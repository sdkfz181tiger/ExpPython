# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import sprite

PLAYER_JUMP_X = 10
PLAYER_JUMP_Y = 300
GROUND_Y      = 30

CAKE_FILES    = [
    "images/cake/cake_01.png",
    "images/cake/cake_02.png",
    "images/cake/cake_03.png"]
CAKE_SPEED_X  = 48
CAKE_PAD_Y    = 42

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width
        self.h = self.window.height
        self.background_color = arcade.color.PAYNE_GREY

        self.cake_y = GROUND_Y + CAKE_PAD_Y

        # Camera
        self.camera = arcade.Camera2D() # プレイヤー用カメラ
        self.camera_gui = arcade.Camera2D() # 固定したカメラ

        # PhysicsEngine
        self.physics = arcade.PymunkPhysicsEngine(
            damping=0.8, gravity=(0, -900))

        # Player
        self.players = arcade.SpriteList()
        self.player = sprite.Player(self.physics, 
            "images/ninja/front_01.png", self.w/2, self.h/2)
        self.players.append(self.player)

        # Coins
        self.coins = arcade.SpriteList()
        for i in range(1):
            x = random.random() * self.w
            y = self.h
            coin = sprite.Coin(self.physics, 
                "images/coin/coin_01.png", x, y)
            #self.coins.append(coin)

        # Blocks
        block_pad_x = 48
        block_total = 8
        block_x = self.w / 2 - block_pad_x * (block_total-1) / 2
        block_y = GROUND_Y
        self.blocks = arcade.SpriteList()
        for i in range(block_total):
            x = block_x + block_pad_x * i
            y = block_y
            block = sprite.Block(self.physics,
                "images/block/block_01.png", x, y)
            self.blocks.append(block)

        # Cakes
        self.cakes = arcade.SpriteList()
        self.spawn_cake() # First Cake!!

        # Info
        self.msg_info = arcade.Text(
            "GAME", self.w/2, self.h-20, 
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Move(WASD)
        if key == arcade.key.A:
            self.physics.set_velocity(self.player, (-PLAYER_JUMP_X, PLAYER_JUMP_Y))
        if key == arcade.key.S:
            self.physics.set_velocity(self.player, (PLAYER_JUMP_X, PLAYER_JUMP_Y))
        
    def on_key_release(self, key, key_modifiers):
        pass
        #self.player.stop() # Stop

    def on_update(self, delta_time):

        self.physics.step(delta_time) # PhysicsEngine

        # Animation
        self.player.update_animation()
        for coin in self.coins:
            coin.update_animation()

        # Player x Cakes
        hit_cakes = arcade.check_for_collision_with_list(
            self.player, self.cakes)
        for cake in hit_cakes:
            if cake.change_dynamic():
                self.spawn_cake() # Spawn

        # Camera
        self.camera.position = arcade.math.lerp_2d(
            self.camera.position, self.player.position, 0.1)

    def on_draw(self):
        self.clear() # Clear

        self.camera.use()
        self.players.draw()
        self.coins.draw()
        self.blocks.draw()
        self.cakes.draw()

        self.camera_gui.use()
        self.msg_info.draw()

    def spawn_cake(self):
        path = random.choice(CAKE_FILES)
        print("spawn_cake:", path)

        x = 0
        y = self.cake_y
        spd_x = CAKE_SPEED_X
        if random.random() < 0.5:
            x = self.w
            spd_x *= -1
        cake = sprite.Cake(self.physics,
            "images/cake/cake_01.png", x, y)
        cake.move(spd_x, 0)
        self.cakes.append(cake)
        self.cake_y += CAKE_PAD_Y # Next

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    window.show_view(GameView(window)) # GameView
    arcade.run()

if __name__ == "__main__":
    main()