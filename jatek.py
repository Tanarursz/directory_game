import os
import json
import random



class Land:
    def __init__(self, name, places):
        self.name = name
        self.places = places
        
    def json_land(self):
        land_data = {
            "name": self.name,
            "places": self.places,
            }

        json_land = json.dumps(land_data, indent=4)
        with open("lands.json", "a") as outfile:
            outfile.write(json_land)
            
    #ToDo áthelyezni generatebe
    def generate_land(self):
        dirs = os.listdir()
        if self.name not in dirs:
            os.makedirs(self.name)

class Place:
    
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        
    def json_place(self):
        place_data = {
            "name": self.name,
            "x": self.x,
            "y": self.y
            }

        json_place = json.dumps(place_data, indent=4)
        with open("places.json", "a") as outfile:
            outfile.write(json_place)
        
    
        

        
    #ToDo áthelyezni generatebe
    def generate_surface(self, land):
        for place in self.places:
            with open(fr"./{land}/{self.name}", "w") as f:
                for i in range(self.y):
                    for j in range(self.x):         
                        esely = random.randint(1, self.x)
                        if esely == 1:
                            f.write("f")
                        elif esely == 5:
                            f.write("k")
                        else:
                            f.write(".")
                    f.write("\n")


class Generate:
    
        

    
    def generate_place(self):
        pass
        
                
        
    def generate_map(self):
        self.generate_land()
        self.generate_place()
        

Land("szarajevo", ["szar.m", "jevo.m"]).json_land()
Place("erdo", 40, 20).json_place()
#bakugan = Generate('saringan', ["fasz.m", "lol.m"])
#bakugan.generate_map()