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
ASTEROID_SPD_MIN = 1.0
ASTEROID_SPD_MAX = 2.0
ASTEROID_DEG_MIN = 60
ASTEROID_DEG_MAX = 120
BULLET_SPD = 3

SPAWN_INTERVAL = 20
SPAWN_LIMIT = 30

# Game
class Game:
    def __init__(self):

        # プレイヤー
        self.ship = sprite.ShipSprite(W/2, H - 24)
        deg = 0 if random.random()<0.5 else 180
        self.ship.move(SHIP_SPD, deg)

        # 隕石
        self.spawn_time = 0
        self.asteroids = []

        # 弾丸
        self.bullets = []

        # Pyxel
        px.init(W, H, title="Hello, Pyxel!!")
        px.load("shooter.pyxres")
        px.run(self.update, self.draw)

    def update(self):

        # Quit
        if px.btnp(px.KEY_Q):
            px.quit()

        # プレイヤー
        self.ship.update()
        self.check_border(self.ship)

        # コントロール
        if px.btnp(px.KEY_SPACE):
            self.action() # Action

        # 隕石
        for asteroid in self.asteroids:
            asteroid.update()
            self.check_border(asteroid)
            
        # 弾丸
        for bullet in self.bullets:
            bullet.update()
            # 画面外削除
            if bullet.y < 0:
                self.bullets.remove(bullet)
                continue
            # 衝突判定
            for asteroid in self.asteroids:
                if asteroid.intersects(bullet):
                    self.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)
                    return

        self.check_spawn() # 隕石の追加

    def draw(self):
        px.cls(0)

        # プレイヤー
        self.ship.draw()

        # 隕石
        for asteroid in self.asteroids:
            asteroid.draw()

        # 弾丸
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
        # インターバル
        self.spawn_time += 1
        if SPAWN_INTERVAL < self.spawn_time:
            self.spawn_time = 0
            if SPAWN_LIMIT < len(self.asteroids): return # Limit
            # 隕石の追加
            x = random.random() * W
            y = 0
            spd = random.uniform(ASTEROID_SPD_MIN, ASTEROID_SPD_MAX)
            deg = random.uniform(ASTEROID_DEG_MIN, ASTEROID_DEG_MAX)
            asteroid = sprite.AsteroidSprite(x, y)
            asteroid.move(spd, deg)
            self.asteroids.append(asteroid)

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