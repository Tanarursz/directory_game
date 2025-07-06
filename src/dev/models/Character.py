class Character:
    def __init__(self, skin="x", here="../dev/modules/map/fasz/erdo.map", coordinates=[1, 1]):
        self.skin = skin
        self.here = here
        self.coordinates = coordinates
        with open(here, "r") as file:
            self.load = [list(section) for section in file.readlines()]

    def spawn(self):
        with open(self.here, "r") as f:
            place = [list(section) for section in f.readlines()]
            place[self.coordinates[0]][self.coordinates[1]] = self.skin
            with open(self.here, "w") as fw:
                for section in place:
                    fw.write("".join(section))

    def see(self):


        for section in self.load:
            print("".join(section),end="")



    def move(self):
        def up():
            self.load[self.coordinates[0]][self.coordinates[1]] = " "
            self.coordinates[0] -= 1
            self.load[self.coordinates[0]][self.coordinates[1]] = "x"

        def down():
            self.load[self.coordinates[0]][self.coordinates[1]] = " "
            self.coordinates[0] += 1
            self.load[self.coordinates[0]][self.coordinates[1]] = "x"

        def right():
            self.load[self.coordinates[0]][self.coordinates[1]] = " "
            self.coordinates[1] += 1
            self.load[self.coordinates[0]][self.coordinates[1]] = "x"

        def left():
            self.load[self.coordinates[0]][self.coordinates[1]] = " "
            self.coordinates[1] -= 1
            self.load[self.coordinates[0]][self.coordinates[1]] = "x"

        where = input()
        if where== "w": up()

        if where=="s": down()

        if where=="a": left()

        if where=="d": right()
