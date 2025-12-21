# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import sprite

PLAYER_SPEED = 90

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width
        self.h = self.window.height

        self.background_color = arcade.color.PAYNE_GREY

        # Camera
        self.camera = arcade.Camera2D() # プレイヤー用カメラ
        self.camera_gui = arcade.Camera2D() # 固定したカメラ

        # Player
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png", 
                             self.w/2, self.h/2)
        self.players.append(self.player)

        # Coin
        self.coins = arcade.SpriteList()
        for i in range(10):
            x = random.random() * self.w
            y = random.random() * self.h
            coin = sprite.Coin("images/coin/coin_01.png", x, y)
            self.coins.append(coin)

         # Info
        self.msg_info = arcade.Text(
            "GAME", 
            self.w/2, self.h-20, 
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Move(WASD)
        if key == arcade.key.W: self.player.move(PLAYER_SPEED, 90, "back")
        if key == arcade.key.A: self.player.move(PLAYER_SPEED, 180, "left")
        if key == arcade.key.S: self.player.move(PLAYER_SPEED, 270, "front")
        if key == arcade.key.D: self.player.move(PLAYER_SPEED, 0, "right")

    def on_key_release(self, key, key_modifiers):
        self.player.stop() # Stop

    def on_update(self, delta_time):

        self.players.update(delta_time)
        self.coins.update(delta_time)

        # プレイヤー用カメラの座標をプレイヤーに追わせる
        self.camera.position = arcade.math.lerp_2d(
            self.camera.position, self.player.position, 0.1)

    def on_draw(self):
        self.clear() # Clear

        self.camera.use() # プレイヤー用カメラを使う
        self.players.draw()
        self.coins.draw()

        self.camera_gui.use() # 固定したカメラを使う
        self.msg_info.draw()

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    window.show_view(GameView(window)) # GameView
    arcade.run()

if __name__ == "__main__":
    main()