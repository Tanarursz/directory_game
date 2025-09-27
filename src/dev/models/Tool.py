# name = the tool name
# tbreak = the list of things that the tool can break)
# noise = the noise it makes, when u hit an object
# durability = the tool durability, its getting lower on hits
# status = it has 3 states (new, used, broken) the efficenty is getting lower by durability

class Tool:
    def __init__(self, name, noise, durability: int, tbreak: list):
        self.name = name
        self.noise = noise
        self.durability, self.max_durability = durability
        self.tbreak = tbreak
        self.status = "new"

    # first if checks if the durability is at half way then give the used status
    # elif is for broken status, when the durability lower or equal with 0.

    def durability_check(self):
        if self.durability <= self.max_durability // 2:
            print('low durability')
            self.status = "used"
        elif self.durability <= 0:
            print(f"{self.name} is broken")
            self.status = "broken"
            return False

        return True

        # the tool got "new" status and full durability

    def repair(self):
        self.status = "new"
        self.durability = self.max_durability()
        print(f"{self.name} repaired")

    # id = the thing id that can or cannot break (bool)
    # in the first if we check if the id in the "id pool" (tbreak)
    # if its in the durability checks for breaking if it is the lower the durability and return True (it can break)
    def can_break(self, id):
        if id in self.tbreak:
            play(self.noise)
            if self.durability_check():
                self.durability -= 1
                return True

        return False


'''
            jegyzet a töréshez 

  ------------------------   amerre néz a karakter arra tud törni pl  
  |                      |   irány mutató:
  |           f          |          |  <---  felfelé néz
  |           xk         |          •
  |                      |
  ------------------------  

            f               
       üres X k            X <- a karakter
          üres             f,k <- valamilyen objektim "+" ebben a formátumban látja őket a karakter


  '''