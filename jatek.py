import os
import json
import random
from os import mkdir


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



            
    #ToDo áthelyezni generatebe


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
World().generate_world()
Place("fasz", "erdo.map",50, 30).json_place()
Place("kope", "kishegy.map", 50, 30).json_place()
Land("fasz").json_land()
Land("kope").json_land()
