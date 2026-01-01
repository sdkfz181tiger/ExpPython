# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite

W, H = 160, 120 # ゲーム画面の幅、高さ
SHIP_SPD = 1.4 # プレイヤーの速度

ASTEROID_INTERVAL = 20 # 隕石の発生間隔
ASTEROID_LIMIT = 30 # 隕石の最大数

ASTEROID_SPD_MIN = 1.0 # 隕石の最低速度
ASTEROID_SPD_MAX = 2.0 # 隕石の最高速度
ASTEROID_DEG_MIN = 30 # 隕石の最低角度
ASTEROID_DEG_MAX = 150 # 隕石の最高角度

BULLET_SPD = 3 # 弾丸の速度

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # ゲームオーバーフラグ
        self.game_over_flg = False

        # スコアを初期化
        self.score = 0

        # プレイヤーを初期化
        self.ship = sprite.ShipSprite(W/2, H - 40)
        deg = 0 if random.random()<0.5 else 180
        self.ship.move(SHIP_SPD, deg)

        # 隕石
        self.asteroid_time = 0
        self.asteroids = []

        # 弾丸
        self.bullets = []

        # Pyxel
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("shooter.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # ゲームオーバー
        if self.game_over_flg:
            return

        # プレイヤーを更新
        self.ship.update()
        self.control_ship()
        self.overlap_spr(self.ship)

        self.check_interval() # 隕石の追加

        # 隕石の更新
        for asteroid in self.asteroids:
            asteroid.update()
            self.overlap_spr(asteroid)
            # 衝突判定(隕石 x プレイヤー)
            if asteroid.intersects(self.ship):
                self.game_over_flg = True # ゲームオーバー
            
        # 弾丸の更新(逆順)
        for bullet in self.bullets[::-1]:
            bullet.update()
            # 画面外削除
            if bullet.y < 0:
                self.bullets.remove(bullet)
                continue
            # 衝突判定(弾丸 x 隕石)
            for asteroid in self.asteroids[::-1]:
                if asteroid.intersects(bullet):
                    self.score += 1 # スコア
                    self.bullets.remove(bullet)
                    self.asteroids.remove(asteroid)
                    return

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # ゲームオーバー
        if self.game_over_flg:
            msg = "GAME OVER"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 13)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 12)

        # プレイヤーを描画
        self.ship.draw()

        # 隕石の描画
        for asteroid in self.asteroids:
            asteroid.draw()

        # 弾丸の描画
        for bullet in self.bullets:
            bullet.draw()

    def control_ship(self):
        """ アクション """
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.ship.flip_x() # 移動反転
            # 弾丸発射
            bullet = sprite.BulletSprite(self.ship.x, self.ship.y)
            bullet.move(BULLET_SPD, 270)
            self.bullets.append(bullet)

    def overlap_spr(self, spr):
        """ 画面外に出たら反対側へ """
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

    def check_interval(self):
        # 隕石の出現間隔
        self.asteroid_time += 1
        if self.asteroid_time < ASTEROID_INTERVAL: return
        self.asteroid_time = 0
        # 隕石の最大数を超えない範囲で
        if ASTEROID_LIMIT < len(self.asteroids): return
        # 隕石の追加
        x = random.random() * W
        y = 0
        spd = random.uniform(ASTEROID_SPD_MIN, ASTEROID_SPD_MAX)
        deg = random.uniform(ASTEROID_DEG_MIN, ASTEROID_DEG_MAX)
        asteroid = sprite.AsteroidSprite(x, y)
        asteroid.move(spd, deg)
        self.asteroids.append(asteroid)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()