from src.dev.models.Place import Place
from src.dev.models.File import File
from src.dev.models.World import World
from src.dev.models.Land import Land
from src.dev.models.Character import Character


File().generate_json()
Place("fasz", "erdo.map",30, 10).json_place()
Place("kope", "kishegy.map", 30, 10).json_place()
World().generate_world()
Land("fasz").json_land()
Land("kope").json_land()
Character().spawn()


if __name__ == "__main__":
    play = True
    a = Character()
    while play:
        a.see()
        a.move()

# ToDO megjegyezni milyen hely volt előtte
# ToDO Szeparálni a fájlokat
# ToDO Save Game funkcio
# ToDO Collision
