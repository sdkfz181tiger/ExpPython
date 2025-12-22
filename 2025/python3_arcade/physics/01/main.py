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

        # プレイヤー
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png", 
                             self.w/2, self.h/2)
        self.players.append(self.player)

        # 小判
        self.coins = arcade.SpriteList()
        for i in range(10):
            x = random.random() * self.w
            y = self.h
            coin = sprite.Coin("images/coin/coin_01.png", x, y)
            self.coins.append(coin)

        # ブロック
        block_pad_x = 48
        block_total = 8
        block_x = self.w / 2 - block_pad_x * (block_total-1) / 2
        block_y = 30
        self.blocks = arcade.SpriteList()
        for i in range(block_total):
            x = block_x + block_pad_x * i
            y = block_y
            block = sprite.Block("images/block/block_01.png", x, y)
            self.blocks.append(block)

        # Info
        self.msg_info = arcade.Text(
            "GAME", 
            self.w/2, self.h-20, 
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

        # 物理エンジンを作る
        self.physics = arcade.PymunkPhysicsEngine(damping=0.8, gravity=(0, -900))
        # プレイヤーを追加
        self.physics.add_sprite(self.player, 
            friction=1.0, collision_type="player")
        # 小判を追加
        for coin in self.coins:
            self.physics.add_sprite(coin,
                friction=1.0, collision_type="wall",
                body_type=arcade.PymunkPhysicsEngine.DYNAMIC)
        # ブロックを追加
        for block in self.blocks:
            self.physics.add_sprite(block,
                friction=1.0, collision_type="wall",
                body_type=arcade.PymunkPhysicsEngine.STATIC)

    def on_key_press(self, key, key_modifiers):
        # Move(WASD)
        if key == arcade.key.W: self.player.move(PLAYER_SPEED, 90, "back")
        if key == arcade.key.A: self.player.move(PLAYER_SPEED, 180, "left")
        if key == arcade.key.S: self.player.move(PLAYER_SPEED, 270, "front")
        if key == arcade.key.D: self.player.move(PLAYER_SPEED, 0, "right")

    def on_key_release(self, key, key_modifiers):
        self.player.stop() # Stop

    def on_update(self, delta_time):

        self.physics.step() # 物理エンジンを進める

        # Camera
        self.camera.position = arcade.math.lerp_2d(
            self.camera.position, self.player.position, 0.1)

    def on_draw(self):
        self.clear() # Clear

        self.camera.use()
        self.players.draw()
        self.coins.draw()
        self.blocks.draw()

        self.camera_gui.use()
        self.msg_info.draw()

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    window.show_view(GameView(window)) # GameView
    arcade.run()

if __name__ == "__main__":
    main()