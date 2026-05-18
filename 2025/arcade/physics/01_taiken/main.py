# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import sprite

PLAYER_JUMP_X = 10
PLAYER_JUMP_Y = 400

CAKE_FILES    = [
    "images/cake_x2/cake_01.png",
    "images/cake_x2/cake_02.png",
    "images/cake_x2/cake_02.png",
    "images/cake_x2/cake_03.png",
    "images/cake_x2/cake_03.png",
    "images/cake_x2/cake_03.png"]
CAKE_SPEED_X  = 64
CAKE_PAD_Y    = 24
CAKE_INTERVAL = 3.0

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width
        self.h = self.window.height
        self.background_color = arcade.color.PAYNE_GREY

        self.cake_y = self.h / 2
        self.cake_interval = CAKE_INTERVAL

        # Camera
        self.camera = arcade.Camera2D() # プレイヤー用カメラ
        self.camera_gui = arcade.Camera2D() # 固定したカメラ

        # PhysicsEngine
        self.physics = arcade.PymunkPhysicsEngine(
            damping=0.8, gravity=(0, -900))

        # Player
        self.players = arcade.SpriteList()
        self.player = sprite.Player(self.physics, 
            "images/cake_x2/front_01.png", self.w/2, self.h/2 + 48)
        self.players.append(self.player)

        # Table
        self.blocks = arcade.SpriteList()
        table = sprite.Block(self.physics,
                "images/cake_x2/table_01.png", self.w/2, self.h/2 - 64)
        self.blocks.append(table)

        # Cakes
        self.cakes = arcade.SpriteList()

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
        self.players.update_animation(delta_time)

        # Player x Cakes
        hit_cakes = arcade.check_for_collision_with_list(
            self.player, self.cakes)
        for cake in hit_cakes:
            if cake.change_dynamic():
                self.cake_interval = CAKE_INTERVAL

        # Spawn
        if 0.0 < self.cake_interval:
            self.cake_interval -= delta_time
            if self.cake_interval < 0.0:
                self.spawn_cake() # Spawn

        # Camera
        self.camera.position = arcade.math.lerp_2d(
            self.camera.position, self.player.position, 0.1)

    def on_draw(self):
        self.clear() # Clear

        self.camera.use()
        arcade.draw_line(
            0, self.cake_y, self.w, self.cake_y, 
            (255, 255, 255, 100), 1)

        self.players.draw()
        self.blocks.draw()
        self.cakes.draw()

        # Debug
        self.players.draw_hit_boxes()

        self.camera_gui.use()
        self.msg_info.draw()

    def spawn_cake(self):
        path = random.choice(CAKE_FILES)
        x = 0
        y = self.cake_y + CAKE_PAD_Y
        spd_x = CAKE_SPEED_X
        if random.random() < 0.5:
            x = self.w
            spd_x *= -1
        cake = sprite.Cake(self.physics,
            path, x, y)
        cake.move(spd_x, 0)
        self.cakes.append(cake)

        highest_y = 0
        for cake in self.cakes:
            if highest_y < self.cake_y:
                highest_y = cake.center_y
        self.cake_y = highest_y + CAKE_PAD_Y

def main():
    """ メイン処理 """
    window = arcade.Window(480, 480, "Hello, Arcade!!")
    window.show_view(GameView(window)) # GameView
    arcade.run()

if __name__ == "__main__":
    main()