from src.dev.models.Place import Place
from src.dev.models.File import File
from src.dev.models.World import World
from src.dev.models.Land import Land
from src.dev.models.Character import Character
from blessed import Terminal




File().generate_json()
Land("fasz").json_land()
Land("kope").json_land()
Place("fasz", "erdo.map",70, 40).json_place()
Place("kope", "kishegy.map", 50, 20).json_place()
World().generate_world()

Character().spawn()

term = Terminal()


def main():

    a = Character()
    with term.cbreak(), term.hidden_cursor():
        while True:
            print(term.normal_cursor(), end="\033c")
            print(term.home + term.clear() + a.see(), end="\033c")

            key = term.inkey(timeout=0.1)
            if not key:
                continue

            if key.lower() == 'q':
                break
            elif key.lower() == 'w':
                a.load[a.coordinates[0]][a.coordinates[1]] = " "
                a.coordinates[0] -= 1
                a.load[a.coordinates[0]][a.coordinates[1]] = "x"
            elif key.lower() == 'a':
                a.load[a.coordinates[0]][a.coordinates[1]] = " "
                a.coordinates[1] -= 1
                a.load[a.coordinates[0]][a.coordinates[1]] = "x"
            elif key.lower() == 's':
                a.load[a.coordinates[0]][a.coordinates[1]] = " "
                a.coordinates[0] += 1
                a.load[a.coordinates[0]][a.coordinates[1]] = "x"
            elif key.lower() == 'd':
                a.load[a.coordinates[0]][a.coordinates[1]] = " "
                a.coordinates[1] += 1
                a.load[a.coordinates[0]][a.coordinates[1]] = "x"

if __name__ == "__main__":
    main()




# ToDO megjegyezni milyen hely volt előtte
# ToDO mozgás megjavitása
# ToDO Szeparálni a fájlokat
# ToDO Save Game funkcio
# ToDO Collision
