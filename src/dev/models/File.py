import json
import os


class File:

    @staticmethod
    def generate_json():
        def generate_lands_json():
            if not os.path.exists("./src/lands.json"):
                dictionary = {
                    "lands": []
                }
                with open("./src/lands.json", "w") as file:
                    json.dump(dictionary, file, indent=4)

        def generate_places_json():
            if not os.path.exists("./src/places.json"):

                dictionary = {
                    "places": []
                }
                with open("./src/places.json", "w") as file:
                    json.dump(dictionary,file, indent=4)

        generate_lands_json()
        generate_places_json()

    @staticmethod
    def delete_json():
        def delete_lands_json():
            if os.path.exists("./src/lands.json"):
                os.remove("./src/lands.json")
        def delete_places_json():
            if os.path.exists("./src/places.json"):
             os.remove("./src/places.json")
        delete_places_json()
        delete_lands_json()