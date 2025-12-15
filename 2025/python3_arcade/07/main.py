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

        # Sprites
        self.sprites = arcade.SpriteList()

        # Player
        self.player = sprite.Ninja("images/ninja/front_01.png",
                                   x=W/2, y=H/2,
                                   scale=SPRITE_SCALE)
        self.sprites.append(self.player)

        # Coins
        for i in range(10):
            x = random.random() * W
            y = random.random() * H
            self.coin = sprite.Coin("images/coin/coin_01.png",
                                    x=x, y=y,
                                    scale=SPRITE_SCALE)
            self.sprites.append(self.coin)

    def on_key_press(self, key, key_modifiers):
        self.utility.key_press(key) # Utility

        # Move(WASD)
        if key == arcade.key.W: self.player.move(60, 90, "back")
        if key == arcade.key.A: self.player.move(60, 180, "left")
        if key == arcade.key.S: self.player.move(60, 270, "front")
        if key == arcade.key.D: self.player.move(60, 0, "right")

    def on_key_release(self, key, key_modifiers):
        self.player.stop() # Stop

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