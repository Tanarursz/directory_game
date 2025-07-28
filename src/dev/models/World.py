import random
import os
import json


class World:
    def __init__(self):
        with open("./src/lands.json", "r+") as file: self.lands = json.load(file)
        with open("./src/places.json", "r+") as file: self.places = json.load(file)

    def generate_world(self):

        def generate_land():
            for land in self.lands["lands"]:
                if not os.path.exists(fr"./src/dev/modules/map/{land['name']}"):
                    os.makedirs(fr"./src/dev/modules/map/{land['name']}")

        def generate_place():
            for place in self.places["places"]:
                with open(fr"./src/dev/modules/map/{place['land']}/{place['name']}", "w") as f:
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
