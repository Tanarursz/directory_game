class Character:
    def __init__(self, skin="x", here="./src/dev/modules/map/fasz/erdo.map", coordinates=[5, 1]): # COORDINATES[0] ELEME AZ Y
        self.skin = skin
        self.here = here
        self.coordinates = coordinates
        with open(here, "r") as file:
            self.load = [list(section) for section in file.readlines()]

    def spawn(self):
            self.load[self.coordinates[0]][self.coordinates[1]] = self.skin
            with open(self.here, "w") as fw:
                for section in self.load:
                    fw.write("".join(section))



    def radius(self, valami):
        pass

    def see(self, night=False):
        palya = ""

        for y, section in enumerate(self.load):
            if night:
                for x, char in enumerate(section):
                    if char == self.skin or (abs(x - self.coordinates[1]) <= 2 and abs(y - self.coordinates[0]) <= 1):
                        palya += char
                    else:
                        palya += " "

                palya += "\n"
            else:
                palya += "".join(section)
        return palya

    # ToDO Tovább fejlesztett collision (kölön osztály az objektumoknak és a saját helyzetükkel lehgyenek ellátva), tulajdonságok (törhető vagy nem, átmászható vagy nem, be lehet e menni)
    def move(self, keym):
        collista = ["f", "k", "|", "-"]

        if keym.lower() == 'w' and self.load[self.coordinates[0]-1][self.coordinates[1]] not in collista:
            self.load[self.coordinates[0]][self.coordinates[1]] = " "
            self.coordinates[0] -= 1
            self.load[self.coordinates[0]][self.coordinates[1]] = "x"
        elif keym.lower() == 'a' and self.load[self.coordinates[0]][self.coordinates[1]-1] not in collista:
            self.load[self.coordinates[0]][self.coordinates[1]] = " "
            self.coordinates[1] -= 1
            self.load[self.coordinates[0]][self.coordinates[1]] = "x"
        elif keym.lower() == 's' and self.load[self.coordinates[0] +1][self.coordinates[1]] not in collista:
            self.load[self.coordinates[0]][self.coordinates[1]] = " "
            self.coordinates[0] += 1
            self.load[self.coordinates[0]][self.coordinates[1]] = "x"
        elif keym.lower() == 'd' and self.load[self.coordinates[0]][self.coordinates[1]+1] not in collista:
            self.load[self.coordinates[0]][self.coordinates[1]] = " "
            self.coordinates[1] += 1
            self.load[self.coordinates[0]][self.coordinates[1]] = "x"


