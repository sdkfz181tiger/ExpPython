# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import random
import math

class BaseSprite():

    def __init__(self, filename, x, y):
        #super().__init__(filename)
        self.filename = filename
        # Position
        self.center_x = x
        self.center_y = y

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

class Block(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
