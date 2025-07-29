import json


class Place:
    Places =  []
    def __init__(self, land, name, x, y):
        self.land = land
        self.name = name
        self.x = x
        self.y = y
        Place.Places.append(self)

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
