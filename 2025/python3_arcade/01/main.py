# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import src.sprite as sprite
import src.title as title
import src.utility as utility

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    window.show_view(title.TitleView(window)) # TitleView
    arcade.run()

if __name__ == "__main__":
    main()