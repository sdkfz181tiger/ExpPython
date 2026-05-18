# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import sprite
import utility

PLAYER_JUMP_X = 10
PLAYER_JUMP_Y = 400

CAKE_SPEED_X_MIN = 64
CAKE_SPEED_X_MAX = 96
CAKE_PAD_Y       = 24
CAKE_INTERVAL    = 2.0
CAKE_FILES = [
    "images/cake_x2/cake_01.png",
    "images/cake_x2/cake_02.png",
    "images/cake_x2/cake_02.png",
    "images/cake_x2/cake_03.png",
    "images/cake_x2/cake_03.png",
    "images/cake_x2/cake_03.png"]

STAR_FILES = [
    "images/cake_x2/star_01.png",
    "images/cake_x2/star_02.png",
    "images/cake_x2/star_03.png",
    "images/cake_x2/star_04.png"]

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width
        self.h = self.window.height
        self.background_color = arcade.color.POMP_AND_POWER

        self.ready_flg = True
        self.cake_y = self.h / 2
        self.cake_interval = CAKE_INTERVAL

        # UtilSounds
        self.sounds = utility.UtilSounds()
        self.sounds.load_sound("ready", "sounds/bgm_ready.ogg")
        self.sounds.load_sound("game",  "sounds/bgm_game.ogg")
        self.sounds.load_sound("coin",  "sounds/se_coin.ogg")
        self.sounds.load_sound("jump",  "sounds/se_jump.ogg")
        self.sounds.load_sound("land",  "sounds/se_land.ogg")
        self.sounds.play("ready", volume=0.2)

        # Camera
        self.camera = arcade.Camera2D() # プレイヤー用カメラ
        self.camera_gui = arcade.Camera2D() # 固定したカメラ

        # PhysicsEngine
        self.physics = arcade.PymunkPhysicsEngine(
            damping=0.8, gravity=(0, -900))

        # SpriteList
        self.backgrounds = arcade.SpriteList()
        self.players = arcade.SpriteList()
        self.blocks = arcade.SpriteList()
        self.cakes = arcade.SpriteList()

        # Carpet
        carpet = sprite.Background(
            "images/cake_x2/carpet_01.png", self.w/2, 50)
        self.backgrounds.append(carpet)

        # Stars
        for i in range(16):
            x = self.camera.position.x - self.w/2 + random.randrange(int(self.w))
            y = self.camera.position.y + random.randrange(int(self.h*2))
            file = random.choice(STAR_FILES)
            star = sprite.Background(file, x, y)
            self.backgrounds.append(star)

        # Player
        self.player = sprite.Player(self.physics, 
            "images/cake_x2/land_01.png", self.w/2, self.h/2 + 34)
        self.players.append(self.player)

        # Table
        table = sprite.Block(self.physics,
                "images/cake_x2/table_01.png", self.w/2, self.h/2 - 64)
        self.blocks.append(table)

        # Info
        self.msg_info = arcade.Text(
            "PRESS TO START!!", self.w/2, self.h-20, 
            arcade.color.WHITE, 16,
            anchor_x="center", anchor_y="top")


    def on_key_press(self, key, key_modifiers):

        # Ready to Start!!
        if self.ready_flg == True:
            self.ready_flg = False
            self.sounds.stop("ready")
            self.sounds.play("game", loop=True, volume=0.2)
            return

        # Move(WASD)
        if key == arcade.key.A:
            self.physics.set_velocity(self.player, (-PLAYER_JUMP_X, PLAYER_JUMP_Y))
            self.player.change_animation("jump")
            self.sounds.play("jump")
        if key == arcade.key.S:
            self.physics.set_velocity(self.player, (PLAYER_JUMP_X, PLAYER_JUMP_Y))
            self.player.change_animation("jump")
            self.sounds.play("jump")
        
    def on_key_release(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):
        if self.ready_flg == True: return

        # Cakes
        self.msg_info.text = "CAKES: {}".format(len(self.cakes))

        self.physics.step(delta_time) # PhysicsEngine

        # Animation
        self.players.update_animation(delta_time)

        # Player x Cakes
        hit_cakes = arcade.check_for_collision_with_list(
            self.player, self.cakes)
        for cake in hit_cakes:
            if cake.change_dynamic():
                self.cake_interval = CAKE_INTERVAL
                self.player.change_animation("land")
                self.sounds.play("land")

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
            self.camera.position.x - self.w/2, self.cake_y, 
            self.camera.position.x + self.w/2, self.cake_y, 
            (255, 255, 255, 100), 1)

        self.backgrounds.draw()
        self.players.draw()
        self.blocks.draw()
        self.cakes.draw()

        # Debug
        self.players.draw_hit_boxes()
        self.blocks.draw_hit_boxes()
        self.cakes.draw_hit_boxes()

        self.camera_gui.use()
        self.msg_info.draw()

    def spawn_cake(self):
        path = random.choice(CAKE_FILES)
        x = 0
        y = self.cake_y + CAKE_PAD_Y
        spd_x = random.randrange(CAKE_SPEED_X_MIN, CAKE_SPEED_X_MAX)
        if random.random() < 0.5:
            x = self.w
            spd_x *= -1
        cake = sprite.Cake(self.physics,
            path, x, y)
        cake.move(spd_x, 0)
        self.cakes.append(cake)

        # Highest
        highest_y = 0
        for cake in self.cakes:
            if highest_y < cake.center_y:
                highest_y = cake.center_y
        self.cake_y = highest_y + CAKE_PAD_Y

def main():
    """ メイン処理 """
    window = arcade.Window(480, 480, "Hello, Arcade!!")
    window.show_view(GameView(window)) # GameView
    arcade.run()

if __name__ == "__main__":
    main()