from pydub import AudioSegment
import os
import pygame
import numpy as np

# path = the path for the sound in the library
# format = the fomat to the file, in default its wav but it can be mp3 or something else
# cut = is a boolean, that tells it NEED TO BE CUT, so its not cutted at the moment, need this to change path after cutting
# sound = it load the sound in its format

class Sound:

    def __init__(self, path, format="wav", cut=False):
        self.cut = cut
        self.name = os.path.basename(path)
        self.format = format
        self.path = path
        self.sound = AudioSegment.from_file(self.path, format=self.format)


    # TODO fix
    def cut(self, minute: int):
        target_duration = minute * 60 * 1000

        long_sound = self.sound * (target_duration // len(self.sound) + 1)

        short_sound = long_sound[:target_duration]


        if self.cut:
            self.path = fr".\public\sounds\cut\{minute}{self.name}.{self.format}"


        short_sound.export(fr".\public\sounds\cut\{minute}{self.name}.{self.format}", format=self.format)

    # change the volume of the sound
    def volume(self, decibel):
        if decibel < 0:
             self.sound -= decibel
        else:
            self.sound += decibel

    # fade the sound with an amount
    def fade(self, infade=0, outfade=0):
        self.sound = self.sound.fade_in(2000).fade_out(2000)

    # plays the sound
    def play(self):
        pygame.mixer.Sound(self.path).play()




