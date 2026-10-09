import pyxel
import sprite

# Appクラス
class App:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="HELLO PYXEL!!")

        self.w = pyxel.width
        self.h = pyxel.height

        # Asteroids
        self.asteroids = []
        for i in range(5):
            # Asteroid
            asteroid = sprite.Sprite(self.w/2, self.h/2, 2, 8)
            self.asteroids.append(asteroid)
            # Move
            deg = pyxel.rndi(0, 360)
            asteroid.move(2, deg)
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        for asteroid in self.asteroids:
            asteroid.update()
            self.overwrap(asteroid)


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        for asteroid in self.asteroids:
            asteroid.draw()


    def overwrap(self, spr):
        """ 画面外判定 """
        if self.w < spr.x:
            spr.x = 0
        if spr.x < 0:
            spr.x = self.w
        if self.h < spr.y:
            spr.y = 0
        if spr.y < 0:
            spr.y = self.h


# Appクラスを初期化
App()