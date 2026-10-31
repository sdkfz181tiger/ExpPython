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

        # Asteroids
        self.asteroids = []
        for i in range(5):
            # Asteroid
            asteroid = utility.BaseSprite(0, 0, 8, 0, 8, 8)
            self.asteroids.append(asteroid)
            # Move
            deg = pyxel.rndi(0, 360)
            asteroid.move(1, deg)

        self.total = len(self.asteroids) # Total
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        # Pause
        if self.pause == True:
            return

        # Asteroids
        for asteroid in self.asteroids:
            asteroid.update()
            self.overlap(asteroid)

        # Click
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            m_x = pyxel.mouse_x
            m_y = pyxel.mouse_y
            for asteroid in self.asteroids:
                if asteroid.is_inside(m_x, m_y):
                    # Stop
                    asteroid.x = 0
                    asteroid.y = 0
                    asteroid.stop()
                    # Total
                    self.total -= 1
                    if self.total <= 0:
                        self.pause = True


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # Mouse
        m_x = pyxel.mouse_x
        m_y = pyxel.mouse_y
        pyxel.circ(m_x, m_y, 1, 7)

        # Asteroids
        for asteroid in self.asteroids:
            asteroid.draw()

        # Total
        pyxel.text(5, 5, f"TOTAL:{self.total}", 7)

        # Game Clear
        if self.pause and self.total <= 0:
            pyxel.text(70, 5, f"GAME CLEAR!!", 7)


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