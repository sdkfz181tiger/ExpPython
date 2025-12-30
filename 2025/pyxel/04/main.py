# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel as px
import math
import random
import sprite

W, H = 160, 120

SHIP_SPD = 1.4
INVADER_SPD_MIN = 1.0
INVADER_SPD_MAX = 2.0
BULLET_SPD = 3

SPAWN_INTERVAL = 20
SPAWN_LIMIT = 30

# Game
class Game:
    def __init__(self):

        # Sprites
        self.sprites = []

        # Ship
        self.ship = sprite.ShipSprite(W/2, H - 24)
        deg = 0 if random.random()<0.5 else 180
        self.ship.move(SHIP_SPD, deg)

        # Invaders
        self.spawn_time = 0
        self.invaders = []

        # Bullets
        self.bullets = []

        # Pyxel
        px.init(W, H, title="Hello, Pyxel!!")
        px.load("shooter.pyxres")
        px.run(self.update, self.draw)

    def update(self):

        # Quit
        if px.btnp(px.KEY_Q):
            px.quit()

        # Ship
        self.ship.update()
        self.check_border(self.ship)

        # Control
        if px.btnp(px.KEY_SPACE):
            self.action() # Action

        # Invaders
        for invader in self.invaders:
            invader.update()
            self.check_border(invader)
            # Remove
            if H < invader.y:
                self.invaders.remove(invader)
            
        # Bullets
        for bullet in self.bullets:
            bullet.update()
            # Remove
            if bullet.y < 0:
                self.bullets.remove(bullet)
                continue
            # x Invaders
            for invader in self.invaders:
                if invader.intersects(bullet):
                    self.bullets.remove(bullet)
                    self.invaders.remove(invader)
                    return

        self.check_spawn() # Spawn

    def draw(self):
        px.cls(0)

        # Ship
        self.ship.draw()

        # Invaders
        for invader in self.invaders:
            invader.draw()

        # Bullets
        for bullet in self.bullets:
            bullet.draw()

    def check_border(self, spr):
        """ 画面端処理 """
        if spr.x < -spr.w: 
            spr.x = W
            return
        if W < spr.x:
            spr.x = -spr.w
            return
        if spr.y < -spr.h:
            spr.y = H
            return
        if H < spr.y:
            spr.y = -spr.h
            return

    def check_spawn(self):
        # Interval
        self.spawn_time += 1
        if SPAWN_INTERVAL < self.spawn_time:
            self.spawn_time = 0
            if SPAWN_LIMIT < len(self.invaders): return # Limit
            # Spawn
            x = random.random() * W
            y = 0
            spd = random.uniform(INVADER_SPD_MIN, INVADER_SPD_MAX)
            deg = random.randint(70, 110)
            invader = sprite.InvaderSprite(x, y)
            invader.move(spd, deg)
            self.invaders.append(invader)

    def action(self):
        """ 左右反転 """
        self.ship.flip_x()
        """ 弾丸発射 """
        bullet = sprite.BulletSprite(self.ship.x, self.ship.y)
        bullet.move(BULLET_SPD, 270)
        self.bullets.append(bullet)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()