from colorama import Fore, Back, Style, init
init()

class Menu:
    Main = None

    def __init__(self, name, buttons):
        self.name = name
        self.index = 0
        self.buttons = buttons

    def next(self):
        if self.index >= len(self.buttons) -1:
            self.buttons[-1].fore = Fore.CYAN
            self.buttons[-1].selected = False
            self.buttons[0].fore = Fore.GREEN
            self.buttons[0].selected = True

            self.index = 0
        else:
            self.index += 1
            self.buttons[self.index -1].fore = Fore.CYAN
            self.buttons[self.index -1].selected = False
            self.buttons[self.index].fore = Fore.GREEN
            self.buttons[self.index].selected = True

    def back(self):
        if self.index <= 0:
            self.buttons[0].fore = Fore.CYAN
            self.buttons[0].selected = False
            self.buttons[-1].fore = Fore.GREEN
            self.buttons[-1].selected = True
            self.index = len(self.buttons) - 1
        else:
            self.index -= 1
            self.buttons[self.index +1].fore = Fore.CYAN
            self.buttons[self.index +1].selected = False
            self.buttons[self.index].fore = Fore.GREEN
            self.buttons[self.index].selected = True


    def show(self):
        menustr = f"{" "*8 + self.name}{"\n"*2}"
        for button in self.buttons:
            menustr += " "*8 + button.fore + button.back + button.text + "\n"

        print(menustr)

    def check_selected(self):
        for button in self.buttons:
            if button.selected:
                return button.callback



