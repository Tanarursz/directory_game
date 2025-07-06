import json

class Land:
    def __init__(self, name):
        self.name = name

    def json_land(self):
        land_data = {
            "name": self.name,
        }

        with open("../lands.json", "r+") as file:
            load_data = json.load(file)

            if land_data not in load_data["lands"]:
                load_data["lands"].append(land_data)
                file.seek(0)
                json.dump(load_data, file, indent=4)

