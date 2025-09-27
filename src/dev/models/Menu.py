from colorama import Fore, Back, Style, init
from src.dev.models.Button import Button

init()

class Menu:
    buttons = [Button("option", fore=Fore.GREEN, selected=True), Button("start"), Button("load")]
    index = 0

    @staticmethod
    def next():
        if Menu.index >= len(Menu.buttons) -1:
            Menu.buttons[-1].fore = Fore.CYAN
            Menu.buttons[-1].selected = False
            Menu.buttons[0].fore = Fore.GREEN
            Menu.buttons[0].selected = True

            Menu.index = 0
        else:
            Menu.index += 1
            Menu.buttons[Menu.index -1].fore = Fore.CYAN
            Menu.buttons[Menu.index -1].selected = False
            Menu.buttons[Menu.index].fore = Fore.GREEN
            Menu.buttons[Menu.index].selected = True

    @staticmethod
    def back():
        if Menu.index <= 0:
            Menu.buttons[0].fore = Fore.CYAN
            Menu.buttons[0].selected = False
            Menu.buttons[-1].fore = Fore.GREEN
            Menu.buttons[-1].selected = True
            Menu.index = len(Menu.buttons) - 1
        else:
            Menu.index -= 1
            Menu.buttons[Menu.index +1].fore = Fore.CYAN
            Menu.buttons[Menu.index +1].selected = False
            Menu.buttons[Menu.index].fore = Fore.GREEN
            Menu.buttons[Menu.index].selected = True


    @staticmethod
    def show():
        menustr = ""
        for button in Menu.buttons:
            menustr += button.fore + button.back + button.text + "\n"

        print(menustr)





