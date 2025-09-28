from src.dev.variables import *

# TODO összeített hangokba áthelyezni


nature.volume(0.1)
nature.play_song()

def main():


    Menu.Main = menu
    tics = 0

    with term.cbreak(), term.hidden_cursor():
        while True:
            print(f"{term.home + term.clear()} {Menu.Main.show()}", end="\033c")

            key = term.inkey(timeout=0.1)

            if not key:
                continue

            if key.name == "KEY_ENTER":
                if Menu.Main.buttons[0].selected:
                    break
                exec(Menu.Main.check_selected())

            if key.lower() == 'w':
                Menu.Main.back()

            if key.lower() == 's':
                Menu.Main.next()


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
