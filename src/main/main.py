import pygame.mixer_music

from src.dev.models.Place import Place
from src.dev.models.File import File
from src.dev.models.World import World
from src.dev.models.Land import Land
from src.dev.models.Character import Character
from blessed import Terminal
import curses



File().generate_json()
Land("fasz").json_land()
Land("kope").json_land()
Place("fasz", "erdo.map",10, 10).json_place()
Place("fasz", "mezo.map",10, 10).json_place()
Place("kope", "kishegy.map", 50, 20).json_place()
Place("kope", "nagyhegy.map", 50, 50).json_place()
World().generate_world()


term = Terminal()

# TODO összeített hangokba áthelyezni
natrue = pygame.mixer.Sound(fr".\public\sounds\menu\nature.mp3")

natrue.play(loops=-1)


def main():
    tics = 0
    a = Character()
    with term.cbreak(), term.hidden_cursor():

        while True:

            print(f"{term.home + term.clear() + a.see(tics)} {f"\nAktuális pálya:{tics} {a.place.name}"}{a.detect_object()}", end="\033c")

            key = term.inkey(timeout=0.1)
            if not key:
                continue

            if key.lower() == 'q':
                break
            else:
                a.move(key)
            tics +=1

if __name__ == "__main__":
    main()



# ToDO Tovább fejlesztett collision (kölön osztály az objektumoknak és a saját helyzetükkel lehgyenek ellátva), tulajdonságok (törhető vagy nem, átmászható vagy nem, be lehet e menni)
# ToDO Save Game funkcio
