import json
import os


class File:

    @staticmethod
    # generate json and make the template
    def generate_json():
        # generate lands json template
        def generate_lands_json():
            if not os.path.exists("./src/lands.json"):
                dictionary = {
                    "lands": []
                }
                with open("./src/lands.json", "w") as file:
                    json.dump(dictionary, file, indent=4)
        # generate place json template
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
    # delete the templates
    def delete_json():
        # delete lands template
        def delete_lands_json():
            if os.path.exists("./src/lands.json"):
                os.remove("./src/lands.json")
        # delete place template
        def delete_places_json():
            if os.path.exists("./src/places.json"):
             os.remove("./src/places.json")
        delete_places_json()
        delete_lands_json()