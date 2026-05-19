# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade

# Sound
class UtilSounds:

    def __init__(self):
        self.sounds = {}
        self.players = {}

    def load_sound(self, key, file_name):
        self.sounds[key] = arcade.Sound(file_name)

    def play(self, key, loop=False, volume=0.3):
        if not key in self.sounds: return
        self.players[key] = arcade.play_sound(self.sounds[key], 
            loop=loop, volume=volume)

    def stop(self, key):
        if not key in self.players: return
        self.sounds[key].stop(self.players[key])

    def stop_all(self):
        for key in self.players.keys():
            self.sounds[key].stop(self.players[key])
