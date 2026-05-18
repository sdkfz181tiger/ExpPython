# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import math

class Carpet(arcade.Sprite):

    def __init__(self, filename, x, y):
        super().__init__(filename)
        # Position
        self.center_x = x
        self.center_y = y


class BaseSprite(arcade.Sprite):

    def __init__(self, physics, filename, x, y):
        super().__init__(filename)
        # Physics
        self.physics = physics
        # Position
        self.center_x = x
        self.center_y = y
        # Animation
        self.anim_interval_cnt = 0
        self.anim_interval_limit = 6
        self.anim_textures = {}
        self.anim_key = "" # Key of Animation


    def change_animation(self, key):
        if not key in self.anim_textures: return
        self.anim_key = key
        self.cur_texture = 0
        self.texture = self.anim_textures[self.anim_key][0]


    def update_animation(self, delta_time: float=1/60):
        # Textures
        textures = self.anim_textures[self.anim_key]

        # Interval
        self.anim_interval_cnt += 1
        if self.anim_interval_cnt < self.anim_interval_limit: return
        self.anim_interval_cnt = 0
        # Frames
        self.cur_texture += 1
        if self.cur_texture >= len(textures):
            self.cur_texture = 0
        self.texture = textures[self.cur_texture]

    def stop(self):
        self.physics.set_velocity(self, (0, 0))

    def check_body_type(self, body_type):
        return self.physics.get_physics_object(self).body.body_type == body_type


class Player(BaseSprite):

    def __init__(self, physics, filename, x, y):
        super().__init__(physics, filename, x, y)
        # Physics
        self.physics.add_sprite(self, 
            friction=1.0, collision_type="player")

        self.anim_textures["land"] = [
            arcade.load_texture("images/cake_x2/land_01.png"),
            arcade.load_texture("images/cake_x2/land_02.png"),
            arcade.load_texture("images/cake_x2/land_03.png"),
            arcade.load_texture("images/cake_x2/land_04.png"),
            arcade.load_texture("images/cake_x2/land_05.png"),
        ]

        self.anim_textures["jump"] = [
            arcade.load_texture("images/cake_x2/jump_01.png"),
            arcade.load_texture("images/cake_x2/jump_02.png"),
            arcade.load_texture("images/cake_x2/jump_03.png"),
            arcade.load_texture("images/cake_x2/jump_04.png"),
            arcade.load_texture("images/cake_x2/jump_05.png"),
        ]

        self.change_animation("land")


class Block(BaseSprite):

    def __init__(self, physics, filename, x, y):
        super().__init__(physics, filename, x, y)
        # Physics
        self.physics.add_sprite(self,
            friction=1.0, collision_type="block",
            body_type=arcade.PymunkPhysicsEngine.STATIC)


class Cake(BaseSprite):

    def __init__(self, physics, filename, x, y):
        super().__init__(physics, filename, x, y)
        # Physics
        self.physics.add_sprite(self,
            friction=1.0, collision_type="cake",
            body_type=arcade.PymunkPhysicsEngine.KINEMATIC)

    def move(self, spd_x, spd_y):
        self.physics.set_velocity(self,(spd_x, spd_y))

    def change_dynamic(self):
        if self.check_body_type(arcade.PymunkPhysicsEngine.DYNAMIC): return False
        self.physics.remove_sprite(self)
        self.physics.add_sprite(self,
            friction=1.0, collision_type="cake",
            body_type=arcade.PymunkPhysicsEngine.DYNAMIC)
        return True

