# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math
import random
import sprite
import utility

# キャンバスの幅と高さ
W, H = 480, 320

# タイトル
TITLE = "Hello, Arcade!!"

# Font
FONT_SIZE = 10

SPRITE_SCALE = 1

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY
        self.utility = utility.Utility(W, H) # Utility

        # Player
        self.player = sprite.Ninja("images/ninja_01.png",
                                   x=W/2, y=H/2,
                                   scale=SPRITE_SCALE)
        self.player.load_animation("front", "images/ninja_{:02d}.png", 5)
        self.player.change_animation("front")

        # Sprites
        self.sprites = arcade.SpriteList()
        self.sprites.append(self.player)

    def on_key_press(self, key, key_modifiers):
        self.utility.key_press(key) # Utility

    def on_update(self, delta_time):
        self.utility.update(delta_time) # Utility

        # Update
        for sprite in self.sprites:
            sprite.update(delta_time)

    def on_draw(self):
        self.clear() # Clear
        self.utility.draw_stats() # Utility
        self.sprites.draw() # Draw

def main():
    """ メイン処理 """

    # Window
    window = arcade.Window(W, H, TITLE)

    # GameView
    game = GameView()

    # Show
    window.show_view(game)

    # Run
    arcade.run()

if __name__ == "__main__":
    main()