import os
import pygame

# path = the path for the sound in the library
# format = the fomat to the file, in default its wav but it can be mp3 or something else
# cut = is a boolean, that tells it NEED TO BE CUT, so its not cutted at the moment, need this to change path after cutting
# sound = it load the sound in its format

pygame.mixer.init()
class Sound:
    def __init__(self, path, format="wav"):
        self.name = os.path.basename(path)
        self.format = format
        self.path = path
        self.sound = pygame.mixer.Sound(path)

    # change the volume of the sound
    def volume(self, decibel):
        self.sound.stop()
        self.sound.set_volume(decibel)
        self.sound.play()

    # fade the sound with an amount
    def play_song(self, infade=0):
        self.sound.play(infade)





