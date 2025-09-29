from src.dev.models.Place import Place
from src.dev.models.File import File
from src.dev.models.World import World
from src.dev.models.Land import Land
from blessed import Terminal
from src.dev.models.Sound import Sound
from src.dev.models.Button import Button
from src.dev.models.Menu import Menu
from src.dev.models.Character import Character
from colorama import Fore, Back, init



# Game Making Stuff
File().generate_json()
Land("fasz").json_land()
Land("kope").json_land()
Place("fasz", "erdo.map",10, 10).json_place()
Place("fasz", "mezo.map",10, 10).json_place()
Place("kope", "kishegy.map", 50, 20).json_place()
Place("kope", "nagyhegy.map", 50, 50).json_place()
# World().generate_world()



term = Terminal()

walk = Sound(r".\public\sounds\normal\walking.wav", format="wav")
nature =  Sound(r".\public\sounds\menu\nature.mp3", format="mp3")
humming = Sound(r".\public\sounds\normal\thinking-humming.wav", format="wav")


menu = Menu("MENU", [Button("start", fore=Fore.GREEN, callback="break", selected=True), Button("option", callback='Menu.Main=option'), Button("load", callback='print("faszos")')])
option = Menu("OPTIONS", [Button("start", fore=Fore.GREEN, callback="break", selected=True), Button("volume", callback="nature.volume(1)")])


a = Character()