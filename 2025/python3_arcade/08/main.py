# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import sprite
import random

W, H = 480, 320
TITLE = "Hello, Arcade!!"

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # 背景スプライト
        self.backgrounds = arcade.SpriteList()
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = W/2
        bkg.center_y = H/2
        self.backgrounds.append(bkg)

        # プレイヤースプライト
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=W/2, y=H/2)
        self.players.append(self.player)

        # 小判スプライト
        self.coins = arcade.SpriteList()
        for i in range(10):
            x = random.random() * W
            y = random.random() * H
            coin = sprite.Coin("images/coin/coin_01.png",
                               x=x, y=y)
            self.coins.append(coin)

    def on_key_press(self, key, key_modifiers):
        # Move(WASD)
        if key == arcade.key.W: self.player.move(90, 90)
        if key == arcade.key.A: self.player.move(90, 180)
        if key == arcade.key.S: self.player.move(90, 270)
        if key == arcade.key.D: self.player.move(90, 0)

    def on_key_release(self, key, key_modifiers):
        self.player.stop()

    def on_update(self, delta_time):
        self.players.update(delta_time)
        self.coins.update(delta_time)

        # プレイヤー x コインリスト
        hit_coins = arcade.check_for_collision_with_list(self.player,
                                                         self.coins)
        for coin in hit_coins:
            coin.remove_from_sprite_lists()

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw()
        self.coins.draw()

def main():
    """ メイン処理 """
    window = arcade.Window(W, H, TITLE)
    game = GameView()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()