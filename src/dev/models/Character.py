import os
from src.dev.models.Place import Place
from src.dev.models.Land import Land
import pygame


# ToDO ell kell ezt innen tüntetni (összesített hang)
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=256)
walk = pygame.mixer.Sound(fr".\public\sounds\normal\walking.wav")


#skin = the characters skin that appears in the game
# place = its from the class Place(), if the place is None, automatically get Places[0]
# coordinates = its the starting coordinates for the player1 (COORDIANTES[0] is y)
# load = load is the place where the character is at the moment, but loaded in list form

class Character:
    def __init__(self, skin="x", place=None , coordinates=[5, 1]):
        if place is None:
            place = Place.Places[0] if Place.Places else None
        self.skin = skin
        self.coordinates = coordinates
        self.land =place.land
        self.place = place
        with open(fr"./src/dev/modules/map/{self.land}/{self.place.name}", "r") as file:
            self.load = [list(section) for section in file.readlines()]


        self.spawn()

    # it spawn the character at its coordinates
    def spawn(self):
            self.load[self.coordinates[0]][self.coordinates[1]] = self.skin
            with open(fr"./src/dev/modules/map/{self.land}/{self.place.name}", "w") as fw:
                for section in self.load:
                    fw.write("".join(section))

    # when u leave a map, its switches to the other one in horizontal or vertical
    # it detect what was your last key and then it uses to guess which direction u go
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

    # its detect nearest objects in sight
    def detect_object(self):
        right = self.load[self.coordinates[0]][self.coordinates[1]-1]
        left = self.load[self.coordinates[0]][self.coordinates[1]+1]
        up = self.load[self.coordinates[0]-1][self.coordinates[1]]
        down = self.load[self.coordinates[0]+1][self.coordinates[1]]
        return f"\n {up}  \n{right}X{left}\n {down}"

    # it 'draws' the map line by line and whatch the tics to estimate time
    def see(self, time): # itt is az 'y' az elso
        palya = ""

        for y, section in enumerate(self.load):
            if time > 10:
                # if tich are high enough, it switch to night, u choose when night is, by changing the bigger number
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
    # it defines what key do what moves and do sounds for moving (right now)
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
        walk.play()



