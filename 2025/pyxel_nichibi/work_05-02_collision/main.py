import pyxel
import utility

# Appクラス
class App:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        self.pause = False
        self.w = pyxel.width
        self.h = pyxel.height

        # Player
        self.player = utility.Sprite(self.w/2, self.h/2, 0, 0, 8, 8)

        # Asteroids
        self.asteroids = []
        for i in range(5):
            # Asteroid
            asteroid = utility.Sprite(0, 0, 8, 0, 8, 8)
            self.asteroids.append(asteroid)
            # Move
            deg = pyxel.rndi(0, 360)
            asteroid.move(0.4, deg)
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        # Pause
        if self.pause == True:
            return

        # Player
        self.player.update()
        self.overlap(self.player)

        # Asteroids
        for asteroid in self.asteroids:
            asteroid.update()
            self.overlap(asteroid)

            # Player x Asteroid
            if self.player.collide(asteroid):
                self.pause = True


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        self.player.draw()
        for asteroid in self.asteroids:
            asteroid.draw()


    def overlap(self, spr):
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