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
BULLET_SPD = 3

# Game
class Game:
    def __init__(self):

        # Sprites
        self.sprites = []

        # Ship
        self.ship = sprite.ShipSprite(W/2, H - 24)
        deg = 0 if random.random()<0.5 else 180
        self.ship.move(SHIP_SPD, deg)

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
            
        # Bullets
        for bullet in self.bullets:
            bullet.update()

    def draw(self):
        px.cls(0)

        # Ship
        self.ship.draw()

        # Bullets
        for bullet in self.bullets:
            bullet.draw()

    def check_border(self, spr):
        """ 画面端処理 """
        if spr.x < 0: 
            spr.x = 0
            spr.vx *= -1
            return
        if W < spr.x + spr.w:
            spr.x = W - spr.w
            spr.vx *= -1
            return
        if spr.y < 0:
            spr.y = 0
            spr.vy *= -1
            return
        if H < spr.y + spr.h:
            spr.y = H - spr.h
            spr.vy *= -1
            return

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