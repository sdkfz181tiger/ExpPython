import pyxel
import utility

# Appクラス
class App:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        self.w = pyxel.width
        self.h = pyxel.height

        # Sprite
        self.spr = utility.Sprite(self.w/2, self.h/2, 0, 0, 8, 8)

        # Animation
        self.spr.set_animation("down", [[0, 16], [8, 16], [16, 16], [24, 16]])
        self.spr.set_animation("up", [[0, 24], [8, 24], [16, 24], [24, 24]])
        self.spr.set_animation("right", [[0, 32], [8, 32], [16, 32], [24, 32]])
        self.spr.set_animation("left", [[0, 40], [8, 40], [16, 40], [24, 40]])
        self.spr.set_animation("dead", [[0, 48], [8, 48], [16, 48], [24, 48], None])
        self.spr.start_animation("dead")
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        self.spr.update()

        if self.w < self.spr.x:
            self.spr.x = 0

        if self.spr.x < 0:
            self.spr.x = self.w

        if self.h < self.spr.y:
            self.spr.y = 0

        if self.spr.y < 0:
            self.spr.y = self.h

        if pyxel.btnp(pyxel.KEY_W):
            self.spr.move(1, 270)
            self.spr.start_animation("up")

        if pyxel.btnp(pyxel.KEY_A):
            self.spr.move(1, 180)
            self.spr.start_animation("left")

        if pyxel.btnp(pyxel.KEY_S):
            self.spr.move(1, 90)
            self.spr.start_animation("down")

        if pyxel.btnp(pyxel.KEY_D):
            self.spr.move(1, 0)
            self.spr.start_animation("right")

        if pyxel.btnr(pyxel.KEY_W):
            self.spr.stop()

        if pyxel.btnr(pyxel.KEY_A):
            self.spr.stop()

        if pyxel.btnr(pyxel.KEY_S):
            self.spr.stop()

        if pyxel.btnr(pyxel.KEY_D):
            self.spr.stop()


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        self.spr.draw()


# Appクラスを初期化
App()