import json

# Lands = list to gether all the land to switchpalces, if u make a Land object automatically get in this list
# name = its the name of the land

class Land:
    Lands = []

    def __init__(self, name):
        self.name = name
        Land.Lands.append(self.name)

    # make the land json it self
    def json_land(self):
        land_data = {
            "name": self.name,
        }

        with open("./src/lands.json", "r+") as file:
            load_data = json.load(file)

            if land_data not in load_data["lands"]:
                load_data["lands"].append(land_data)
                file.seek(0)
                json.dump(load_data, file, indent=4)

