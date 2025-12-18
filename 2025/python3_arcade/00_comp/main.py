# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import sprite
import utility

W, H = 480, 320 # ゲーム画面の幅と高さ
TITLE = "Hello, Arcade!!" # タイトル
FONT_SIZE = 10 # フォントサイズ
SPRITE_SCALE = 1 # スプライトの倍率
PLAYER_SPEED = 90 # プレイヤーの速度

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # 背景
        self.backgrounds = arcade.SpriteList()
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = W/2
        bkg.center_y = H/2
        self.backgrounds.append(bkg)

        # Player
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=W/2, y=H/2)
        self.players.append(self.player)

        # Coins
        self.coins = arcade.SpriteList()
        for i in range(10):
            x = random.random() * W
            y = random.random() * H
            coin = sprite.Coin("images/coin/coin_01.png",
                               x=x, y=y)
            self.coins.append(coin)

        self.stats = utility.Stats(W, H) # Stats

    def on_key_press(self, key, key_modifiers):
        self.stats.key_press(key) # Stats

        # Move(WASD)
        if key == arcade.key.W: self.player.move(PLAYER_SPEED, 90, "back")
        if key == arcade.key.A: self.player.move(PLAYER_SPEED, 180, "left")
        if key == arcade.key.S: self.player.move(PLAYER_SPEED, 270, "front")
        if key == arcade.key.D: self.player.move(PLAYER_SPEED, 0, "right")

    def on_key_release(self, key, key_modifiers):
        self.player.stop() # Stop

    def on_update(self, delta_time):

        # Update
        self.players.update()
        self.coins.update()

        # Player x Coins
        hit_coins = arcade.check_for_collision_with_list(self.player,
                                                         self.coins)
        for coin in hit_coins:
            coin.remove_from_sprite_lists()

        self.stats.update(delta_time) # Stats

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw() # Draw
        self.players.draw()
        self.coins.draw()
        self.stats.draw() # Stats

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