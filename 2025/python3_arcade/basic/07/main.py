# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import sprite
import random

class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width
        self.h = self.window.height

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # 背景スプライト
        self.backgrounds = arcade.SpriteList()
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = self.w / 2
        bkg.center_y = self.h / 2
        self.backgrounds.append(bkg)

        # プレイヤースプライト
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=self.w/2, y=self.h/2)
        self.players.append(self.player)

        # 小判スプライト
        self.coins = arcade.SpriteList()
        for i in range(10):
            x = random.random() * self.w # x座標ランダム
            y = random.random() * self.h # y座標ランダム
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
        self.player.stop() # 停止

    def on_update(self, delta_time):
        self.players.update(delta_time)
        self.coins.update(delta_time) # 小判リストを更新

        # プレイヤー x コインリストの衝突判定
        hit_coins = arcade.check_for_collision_with_list(self.player,
                                                         self.coins)
        # 衝突したコインをコインリストから削除
        for coin in hit_coins:
            coin.remove_from_sprite_lists()

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw()
        self.coins.draw() # 小判リストを描画

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    game = GameView(window)
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()