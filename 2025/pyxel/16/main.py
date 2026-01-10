# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite

W, H = 160, 120

START_X = W / 2
START_Y = H / 2 - 10

MODE_TITLE = "title"
MODE_PLAY = "play"
MODE_GAME_OVER = "game_over"

PLAYER_SPD = 1.4
BULLET_SPD = 4

MONSTER_MAX = 10
MONSTERS = [
    {"u": 32, "v": 72, "spd": 0.1,  "think_interval": 60},
    {"u": 48, "v": 72, "spd": 0.12, "think_interval": 90},
    {"u":  0, "v": 80, "spd": 0.14, "think_interval": 120},
    {"u": 16, "v": 80, "spd": 0.16, "think_interval": 150},
    {"u": 32, "v": 80, "spd": 0.18, "think_interval": 180}
]

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # ゲームモード
        self.game_mode = MODE_TITLE

        # プレイヤーを初期化
        self.player = sprite.PlayerSprite(
            START_X, START_Y, 0, 72, PLAYER_SPD, self)

        # ステージを初期化
        self.reset()

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("vampire.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # コントロール
        self.control()

        # プレイ中判定
        if self.game_mode != MODE_PLAY: return

        # プレイヤーを更新
        self.player.update()
        self.overlap_area(self.player)

        # モンスター
        for monster in self.monsters[::-1]:
            monster.update()
            self.overlap_area(monster)
            # x プレイヤー
            if monster.intersects(self.player):
                self.player.stop() # Stop
                self.game_mode = MODE_GAME_OVER

        # 弾丸
        for bullet in self.bullets[::-1]:
            bullet.update()
            if not bullet.is_dead(): continue
            self.bullets.remove(bullet) # Remove

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # タイルマップ
        pyxel.bltm(0, 0, 0, 0, 128, 192, 128, 0)

        # プレイヤーを描画
        self.player.draw()

        # モンスターを描画
        for monster in self.monsters:
            monster.draw()

        # 弾丸
        for bullet in self.bullets:
            bullet.draw()

        # メッセージ
        if self.game_mode == MODE_TITLE:
            msg = "SPACE TO PLAY"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 7)
            msg = "CONTROL: WASD"
            pyxel.text(W/2-len(msg)*2, H/2+10, msg, 7)
        elif self.game_mode == MODE_GAME_OVER:
            msg = "GAME OVER"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 7)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 7)

    def reset(self):
        """ ステージを初期化 """

        # プレイヤー
        self.player.x = START_X
        self.player.y = START_Y

        # モンスター
        self.monsters = []
        for i in range(30):
            x = random.randint(0, W)
            y = random.randint(0, H)
            item = random.choice(MONSTERS)
            u = item["u"]
            v = item["v"]
            spd = item["spd"]
            think_interval = item["think_interval"]
            monster = sprite.Monster(x, y, u, v, spd, think_interval, self.player)
            # 距離を計算する
            distance = monster.get_distance(self.player)
            if distance < 24: continue
            # プレイヤーへの方向を計算する
            direction = monster.get_direction(self.player)
            monster.move(direction)
            self.monsters.append(monster)

        # 弾丸
        self.bullets = []

    def control(self):
        """ コントロール """

        # ゲームループ
        if pyxel.btnp(pyxel.KEY_SPACE):

            # Title -> Play
            if self.game_mode == MODE_TITLE:
                self.game_mode = MODE_PLAY

            # Game Over -> Title
            if self.game_mode == MODE_GAME_OVER:
                self.game_mode = MODE_TITLE
                # Reset
                self.reset()

            return

        # プレイヤー
        if self.game_mode == MODE_PLAY:

            # W
            if pyxel.btnp(pyxel.KEY_W):
                self.player.move(270)
            elif pyxel.btnr(pyxel.KEY_W):
                self.player.stop()
            # A
            if pyxel.btnp(pyxel.KEY_A):
                self.player.move(180)
            elif pyxel.btnr(pyxel.KEY_A):
                self.player.stop()
            # S
            if pyxel.btnp(pyxel.KEY_S):
                self.player.move(90)
            elif pyxel.btnr(pyxel.KEY_S):
                self.player.stop()
            # D
            if pyxel.btnp(pyxel.KEY_D):
                self.player.move(0)
            elif pyxel.btnr(pyxel.KEY_D):
                self.player.stop()

    def overlap_area(self, spr):
        """ オーバーラップ """
        if W < spr.x: spr.x = 0
        if spr.x < 0: spr.x = W
        if H < spr.y: spr.y = 0
        if spr.y < 0: spr.y = H

    def get_nearest_monster(self):
        """ 最も近いモンスターの座標 """
        distance_min = 999
        nearest = None
        for monster in self.monsters:
            distance = monster.get_distance(self.player)
            if distance_min < distance: continue
            distance_min = distance # Nearest
            nearest = monster
        return nearest

    def on_shot_event(self, spr):
        """ 弾丸発射 """
        # 弾丸
        x, y = spr.get_center()
        bullet = sprite.Bullet(x, y, BULLET_SPD)
        monster = self.get_nearest_monster()
        direction = self.player.get_direction(monster)
        bullet.move(direction)
        self.bullets.append(bullet)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()