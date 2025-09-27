import json

# land = its the name of the land NOT an object from class Land
# name = the name of the place
# x, y = its the hight and the width of the place
class Place:
    Places =  []
    def __init__(self, land, name, x, y):
        self.land = land
        self.name = name
        self.x = x
        self.y = y
        Place.Places.append(self)

    # gebenerate the place and its data to the json file
    def json_place(self):
        place_data = {
            "land": self.land,
            "name": self.name,
            "x": self.x,
            "y": self.y
        }

        with open("./src/places.json", "r+") as file:
            load_data = json.load(file)
            if place_data not in load_data["places"]:
                load_data["places"].append(place_data)
                file.seek(0)
                json.dump(load_data, file, indent=4)
