from colorama import Fore, Back, init
init()

class Button:

    def __init__(self, text, callback=None, selected=False,back=Back.BLACK, fore=Fore.CYAN):
        self.text = text
        self.callback = callback
        self.selected = selected
        self.back = back
        self.fore = fore