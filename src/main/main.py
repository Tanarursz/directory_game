from src.dev.models.Place import Place
from src.dev.models.File import File
from src.dev.models.World import World
from src.dev.models.Land import Land
from src.dev.models.Character import Character
from blessed import Terminal




File().generate_json()
Land("fasz").json_land()
Land("kope").json_land()
Place("fasz", "erdo.map",10, 10).json_place()
Place("fasz", "mezo.map",10, 10).json_place()
Place("kope", "kishegy.map", 50, 20).json_place()
Place("kope", "nagyhegy.map", 50, 50).json_place()
World().generate_world()


term = Terminal()


def main():

    a = Character()
    with term.cbreak(), term.hidden_cursor():
        while True:
            print(term.home + term.clear() + a.see(True), end="\033c")

            key = term.inkey(timeout=0.1)
            if not key:
                continue

            if key.lower() == 'q':
                break
            else:
                a.move(key)

if __name__ == "__main__":
    main()



# ToDO Tovább fejlesztett collision (kölön osztály az objektumoknak és a saját helyzetükkel lehgyenek ellátva), tulajdonságok (törhető vagy nem, átmászható vagy nem, be lehet e menni)
# ToDO Save Game funkcio
