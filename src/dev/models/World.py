import random
import os
import json


class World:
    # lands = the json files with all teh land data
    # places = the json files with all the places data
    def __init__(self):
        with open("./src/lands.json", "r+") as file: self.lands = json.load(file)
        with open("./src/places.json", "r+") as file: self.places = json.load(file)

    # generate the word with lands and places
    def generate_world(self):

        # it makes the directory (LAND) if its doesnt existed yet
        def generate_land():
            for land in self.lands["lands"]:
                if not os.path.exists(fr"./src/dev/modules/map/{land['name']}"):
                    os.makedirs(fr"./src/dev/modules/map/{land['name']}")

        '''it generates the land like this
        ------------ 
        | f    f   |
        |          |
        |    k     |
        |          |
        ------------
        
        and write in places-name.map file then its got loaded in the see() function in the Character.py
        it uses random to generate object like tree and stone 
        the player get in later from the spawn function in the Character.py
        
        '''
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
