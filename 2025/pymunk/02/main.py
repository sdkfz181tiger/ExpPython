# coding: utf-8

"""
かじるプログラミング_pymunk
"""

import pymunk
import pyxel
import math
import random

W, H       = 320, 240
FPS        = 32
DELAY_TIME = 1 / FPS
COLOR      = 7 # White

# PyxelDrawOptions
class SimpleDebugDrawOptions(pymunk.SpaceDebugDrawOptions):
    """ DebugDrawOptions for Pyxel """

    def __init__(self, camera=(0, 0)):
        super().__init__()
        # Camera
        self.camera = pymunk.Vec2d(*camera)

    def p(self, v):
        return (int(v.x - self.camera.x), int(v.y - self.camera.y))

    def draw_circle(self, pos, angle, radius, outline_color, fill_color):
        pyxel.circb(int(pos.x), int(pos.y), radius, COLOR)
        end_x = pos.x + math.cos(angle) * radius
        end_y = pos.y + math.sin(angle) * radius
        pyxel.line(pos.x, pos.y, end_x, end_y, COLOR)

    def draw_segment(self, a, b, color):
        pyxel.line(int(a.x), int(a.y), int(b.x), int(b.y), COLOR)

    def draw_fat_segment(self, a, b, radius, outline_color, fill_color):
        pyxel.line(int(a.x), int(a.y), int(b.x), int(b.y), COLOR)

    def draw_polygon(self, verts, radius, outline_color, fill_color):
        n = len(verts)
        if n < 2: return
        for i in range(n):
            v1 = verts[i]
            v2 = verts[(i + 1) % n]
            pyxel.line(v1.x, v1.y, v2.x, v2.y, COLOR)

    def draw_dot(self, size, pos, color):
        pyxel.pset(pos.x, pos.y, COLOR)

# Game
class Game:
    def __init__(self):
        """ Constructor """

        # Pymunk
        self.space = pymunk.Space()
        self.space.gravity = 0, 820
        self.ddo = SimpleDebugDrawOptions() # DebugDraw

        # Segment
        points = [
                (45, H - 120),
                (50, H - 70),
                (W - 50, H - 75)]
        for a, b in zip(points, points[1:]):
            ground = pymunk.Segment(
                self.space.static_body, a, b, 4)
            ground.friction = 1.0
            self.space.add(ground) # Add

        # Box, Circle
        self.create_box(W/2-30,    H/2-64, 16, 32)
        self.create_box(W/2,       H/2-48, 32, 16)
        self.create_circle(W/2,    H/2-64, 8)
        self.create_circle(W/2+48, H/2-96, 16)

        # Pyxel
        pyxel.init(W, H, title="Hello, Pyxel!!", fps=FPS)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.space.step(DELAY_TIME) # Step

    def draw(self):
        # Clear
        pyxel.cls(0)
        self.space.debug_draw(self.ddo) # DebugDraw

    def _create_body(self, x, y):
        body = pymunk.Body()
        body.position = (x, y)
        return body

    def create_box(self, x, y, w, h):
        body = self._create_body(x, y)
        shape = pymunk.Poly.create_box(body, (w, h))
        shape.mass = 10
        self.space.add(body, shape)

    def create_circle(self, x, y, r):
        body = self._create_body(x, y)
        shape = pymunk.Circle(body, r)
        shape.mass = 10
        self.space.add(body, shape)

def main():
    """ Main """
    Game()

if __name__ == "__main__":
    main()