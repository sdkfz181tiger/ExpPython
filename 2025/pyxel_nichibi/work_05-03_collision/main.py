import pyxel
import utility

# Gameクラス
class Game:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        self.pause = False
        self.w = pyxel.width
        self.h = pyxel.height

        self.life = 3 # Life

        # Player
        self.player = utility.BaseSprite(self.w/2, self.h/2, 0, 0, 8, 8)

        # Asteroids
        self.asteroids = []
        for i in range(5):
            # Asteroid
            asteroid = utility.BaseSprite(0, 0, 8, 0, 8, 8)
            self.asteroids.append(asteroid)
            # Move
            deg = pyxel.rndi(0, 360)
            asteroid.move(2, deg)
        
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
                asteroid.x = 0
                asteroid.y = 0
                asteroid.move(2, pyxel.rndi(0, 360))

                self.life -= 1 # Life
                if self.life <= 0:
                    self.pause = True


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        self.player.draw()
        for asteroid in self.asteroids:
            asteroid.draw()

        pyxel.text(5, 5, f"LIFE:{self.life}", 7)


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


# Gameクラスを初期化
Game()