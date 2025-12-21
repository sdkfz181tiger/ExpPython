# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import src.sprite as sprite
import src.utility as utility
import src.title as title

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    view = title.TitleView(window) # TitleView
    window.show_view(view)
    arcade.run()

if __name__ == "__main__":
    main()