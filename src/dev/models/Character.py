import os
from src.dev.models.Place import Place
from src.dev.models.Land import Land

class Character:
    def __init__(self, skin="x", place=None , coordinates=[5, 1]): # COORDINATES[0] ELEME AZ Y
        if place is None:
            place = Place.Places[0] if Place.Places else None
        self.skin = skin
        self.coordinates = coordinates
        self.land =place.land
        self.place = place
        with open(fr"./src/dev/modules/map/{self.land}/{self.place.name}", "r") as file:
            self.load = [list(section) for section in file.readlines()]


        self.spawn()

    def spawn(self):
            self.load[self.coordinates[0]][self.coordinates[1]] = self.skin
            with open(fr"./src/dev/modules/map/{self.land}/{self.place.name}", "w") as fw:
                for section in self.load:
                    fw.write("".join(section))


    def switchplace(self, last_key):
        place_index = Place.Places.index(self.place)
        land_index = Land.Lands.index(self.land)
        if last_key == 'a' and Place.Places[place_index - 1].land == self.land and place_index-1 >= 0:
                self.place = Place.Places[place_index - 1]
                self.coordinates[1] = self.place.x -2


        if last_key == 'd' and place_index < len(Place.Places)-1 and Place.Places[place_index + 1].land == self.land:
                self.place = Place.Places[place_index + 1]
                self.coordinates[1] = self.place.x - (self.place.x -1)


        if last_key == 'w' and  land_index < len(Land.Lands)-1 :
                self.land = Land.Lands[land_index +1]
                for place in Place.Places:
                    if place.land == self.land:
                        self.place = place
                        break
                self.coordinates[0] = self.place.y-2


        if last_key == 's' and land_index - 1 >= 0:
                self.land = Land.Lands[land_index -1]
                for place in Place.Places:
                    if place.land == self.land:
                        self.place = place
                        break
                self.coordinates[0] = 1


        with open(fr"./src/dev/modules/map/{self.land}/{self.place.name}", "r") as file:
            self.load = [list(section) for section in file.readlines()]




    def see(self, night=False): # itt is az 'y' az elso
        palya = ""

        for y, section in enumerate(self.load):
            if night:
                for x, char in enumerate(section):
                    if char == self.skin or (abs(x - self.coordinates[1]) <= 1 and abs(y - self.coordinates[0]) <= 1):
                        palya += char
                    else:
                        palya += " " # karakter középen marad a táj mozog körülötte

                palya += "\n"
            else:
                palya += "".join(section)
        return palya

    # ToDO Tovább fejlesztett collision (kölön osztály az objektumoknak és a saját helyzetükkel lehgyenek ellátva), tulajdonságok (törhető vagy nem, átmászható vagy nem, be lehet e menni)
    def move(self, keym):

        objektumok = ["f", "k"]
        fal = ["|", "-"]

        self.load[self.coordinates[0]][self.coordinates[1]] = " "

        if keym.lower() == 'w' and self.load[self.coordinates[0]-1][self.coordinates[1]] not in objektumok:
            if self.load[self.coordinates[0]-1][self.coordinates[1]] in fal:
                self.switchplace("w")
            else:
                self.coordinates[0] -= 1


        elif keym.lower() == 'a' and self.load[self.coordinates[0]][self.coordinates[1]-1] not in objektumok:
            if self.load[self.coordinates[0]][self.coordinates[1]-1]  in fal:
                self.switchplace("a")
            else:
                self.coordinates[1] -= 1


        elif keym.lower() == 's' and self.load[self.coordinates[0] +1][self.coordinates[1]] not in objektumok:
            if self.load[self.coordinates[0]+1][self.coordinates[1]] in fal:
                self.switchplace("s")
            else:
                self.coordinates[0] += 1


        elif keym.lower() == 'd' and self.load[self.coordinates[0]][self.coordinates[1]+1] not in objektumok:
            if self.load[self.coordinates[0]][self.coordinates[1]+1]  in fal:
                self.switchplace("d")
            else:
                self.coordinates[1] += 1

        try:
            self.load[self.coordinates[0]][self.coordinates[1]] = "x"
        except: #ha olyan helyen jössz vissza ami nincs már a hosszában vagy magasságában a pályának 1,1 re álltja a koordinátákat
            self.coordinates[0] = 1
            self.coordinates[1] = 1
            self.load[self.coordinates[0]][self.coordinates[1]] = "x"


