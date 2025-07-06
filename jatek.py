import csv
import os
import json
import random
import keyboard


class Character:
    def __init__(self, skin="x", here="fasz/erdo.map", coordinates=[1, 1]):
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

class Land:
    def __init__(self, name):

        self.name = name
        
    def json_land(self):

        land_data = {
            "name": self.name,
            }


        with open("lands.json", "r+") as file:
            load_data = json.load(file)

            if land_data not in load_data["lands"]:
                load_data["lands"].append(land_data)
                file.seek(0)
                json.dump(load_data, file, indent=4)



class Place:
    
    def __init__(self, land, name, x, y):
        self.land = land
        self.name = name
        self.x = x
        self.y = y
        
    def json_place(self):


        place_data = {
            "land": self.land,
            "name": self.name,
            "x": self.x,
            "y": self.y
            }

        with open("places.json", "r+") as file:
            load_data = json.load(file)
            if place_data not in load_data["places"]:
                load_data["places"].append(place_data)
                file.seek(0)
                json.dump(load_data, file, indent=4)

    
class World:
    def __init__(self):
        with open("lands.json", "r+") as file: self.lands = json.load(file)
        with open("places.json", "r+") as file: self.places = json.load(file)

    def generate_world(self):

        def generate_land():
            for land in self.lands["lands"]:
                if not os.path.exists(land["name"]):
                    os.makedirs(land["name"])

        def generate_place():
            for place in self.places["places"]:
                with open(fr"./{place["land"]}/{place["name"]}", "w") as f:
                    for i in range(place["y"]):
                        for j in range(place["x"]):
                            esely = random.randint(1, place["x"])

                            if i == 0 or i == place["y"]-1:
                                f.write("-")
                                continue
                            if j == 0 or j == place["x"] -1:
                                f.write("|")
                                continue
                            if esely == 3 and j != place["y"] and i != place["x"]:
                                f.write("f")
                                continue
                            if esely == 5 and j != place["y"] and i != place["x"]:
                                f.write("k")
                                continue

                            else:
                                f.write(" ")
                        f.write("\n")

        generate_land()
        generate_place()




class Json:

    @staticmethod
    def generate_json():
        def generate_lands_json():
            if not os.path.exists("lands.json"):
                dictionary = {
                    "lands": []
                }
                with open("lands.json", "w") as file:
                    json.dump(dictionary, file, indent=4)

        def generate_places_json():
            if not os.path.exists("places.json"):

                dictionary = {
                    "places": []
                }
                with open("places.json", "w") as file:
                    json.dump(dictionary,file, indent=4)

        generate_lands_json()
        generate_places_json()

    @staticmethod
    def delete_json():
        def delete_lands_json():
            if os.path.exists("lands.json"):
                os.remove("lands.json")
        def delete_places_json():
            if os.path.exists("places.json"):
             os.remove("places.json")
        delete_places_json()
        delete_lands_json()


Json().generate_json()
Place("fasz", "erdo.map",30, 10).json_place()
Place("kope", "kishegy.map", 30, 10).json_place()
World().generate_world()
Land("fasz").json_land()
Land("kope").json_land()
Character().spawn()


play = True
a = Character()
while play:
    a.see()
    a.move()

# ToDO megjegyezni milyen hely volt előtte
# ToDO Szeparálni a fájlokat
