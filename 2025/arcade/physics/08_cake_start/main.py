# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import arcade.gui
import random
import sprite
import utility

PLAYER_JUMP_X = 0
PLAYER_JUMP_Y = 400

CAKE_SPEED_X_MIN = 64
CAKE_SPEED_X_MAX = 96
CAKE_PAD_Y       = 48
CAKE_INTERVAL    = 2.0

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width
        self.h = self.window.height
        self.background_color = arcade.color.POMP_AND_POWER

        # UtilSounds
        self.sounds = utility.UtilSounds()

        # Camera
        self.camera = arcade.Camera2D()
        self.camera_gui = arcade.Camera2D()

        # UI
        self.ui_manager = arcade.gui.UIManager()
        btn_retry = arcade.gui.UIFlatButton(
            text="RETRY", width=128, height=32)
        btn_retry.on_click = self.on_click_retry_button

        # Grid
        rows = 10
        cols = 10
        h_spacing = self.w / cols
        v_spacing = self.h / rows
        self.grid = arcade.gui.UIGridLayout(
            column_count=rows, row_count=cols, 
            horizontal_spacing=h_spacing, 
            vertical_spacing=v_spacing
        )
        self.grid.add(btn_retry, column=7, row=9)
        self.anchor = self.ui_manager.add(arcade.gui.UIAnchorLayout())
        self.anchor.add(
            anchor_x="center_x", anchor_y="center_y", child=self.grid)

        self.reset()

    def reset(self):

        self.ready_flg = True
        self.cake_y = self.h / 2 + CAKE_PAD_Y / 2
        self.cake_interval = CAKE_INTERVAL

        self.sounds.stop_all()
        self.sounds.play("ready", volume=0.2)

        # PhysicsEngine
        self.physics = arcade.PymunkPhysicsEngine(
            damping=0.8, gravity=(0, -900))

        # SpriteList
        self.backgrounds = arcade.SpriteList()
        self.blocks = arcade.SpriteList()
        self.players = arcade.SpriteList()
        self.cakes = arcade.SpriteList()

        # Stars
        for i in range(16):
            x = self.camera.position.x - self.w/2 + random.randrange(int(self.w))
            y = self.camera.position.y + random.randrange(int(self.h*2))
            star = sprite.Star(x, y)
            self.backgrounds.append(star)

        # Carpet
        carpet = sprite.Carpet(self.w/2, 50)
        self.backgrounds.append(carpet)

        # ステップ1: Table
        # table = sprite.Table(self.physics, 
        #     self.w/2, self.h/2 - 64)
        # self.blocks.append(table)

        # Player
        self.player = sprite.Player(self.physics, 
            self.w/2, self.h/2 + 34)
        self.players.append(self.player)

        # Info
        self.msg_info = arcade.Text(
            "PRESS KEY TO START!!", self.w/2, self.h-20, 
            arcade.color.WHITE, 16,
            anchor_x="center", anchor_y="top")

    def on_hide_view(self):
        self.ui_manager.disable()

    def on_show_view(self):
        self.ui_manager.enable()

    def on_key_press(self, key, key_modifiers):

        # Ready...
        if self.ready_flg == True:
            self.ready_flg = False
            self.sounds.stop_all()
            self.sounds.play("game", loop=True, volume=0.2)
            return

        # ステップ2: Action
        # if key == arcade.key.A:
        #     self.player.jump(-PLAYER_JUMP_X, PLAYER_JUMP_Y)
        #     self.sounds.play("jump")
        # if key == arcade.key.S:
        #     self.player.jump(PLAYER_JUMP_X, PLAYER_JUMP_Y)
        #     self.sounds.play("jump")

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
                self.player.land()
                self.sounds.play("land")

        # Spawn
        if 0.0 < self.cake_interval:
            self.cake_interval -= delta_time
            if self.cake_interval < 0.0:
                self.spawn_cake() # Spawn

        # Camera
        camera_x = self.camera.position[0]
        camera_y = arcade.math.lerp(
            self.camera.position[1],
            self.player.position[1], 0.1)
        self.camera.position = (camera_x, camera_y)

    def on_draw(self):
        self.clear() # Clear

        self.camera.use()
        arcade.draw_line(
            self.camera.position.x - self.w/2, self.cake_y, 
            self.camera.position.x + self.w/2, self.cake_y, 
            (255, 255, 255, 100), 1)

        self.backgrounds.draw()
        self.blocks.draw()
        self.players.draw()
        self.cakes.draw()

        # Debug
        #self.blocks.draw_hit_boxes()
        #self.players.draw_hit_boxes()
        #self.cakes.draw_hit_boxes()

        self.camera_gui.use()
        self.msg_info.draw()
        self.ui_manager.draw()

    def spawn_cake(self):
        x = 0
        y = self.cake_y + 1
        spd_x = random.randrange(CAKE_SPEED_X_MIN, CAKE_SPEED_X_MAX)
        # ステップ4: Random
        # if random.random() < 0.5:
        #     x = self.w
        #     spd_x *= -1
        # ステップ3: Cake
        # cake = sprite.Cake(self.physics, x, y)
        # cake.move(spd_x, 0)
        # self.cakes.append(cake)
        self.cake_y += CAKE_PAD_Y

    def on_click_retry_button(self, event):
        print("RETRY")
        self.reset()


def main():
    """ メイン処理 """
    window = arcade.Window(320, 480, "Hello, Arcade!!")
    window.show_view(GameView(window)) # GameView
    arcade.run()

if __name__ == "__main__":
    main()