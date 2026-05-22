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

        self.load_sound("ready", "sounds/bgm_ready.ogg")
        self.load_sound("game",  "sounds/bgm_game.ogg")
        self.load_sound("coin",  "sounds/se_coin.ogg")
        self.load_sound("jump",  "sounds/se_jump.ogg")
        self.load_sound("land",  "sounds/se_land.ogg")

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
