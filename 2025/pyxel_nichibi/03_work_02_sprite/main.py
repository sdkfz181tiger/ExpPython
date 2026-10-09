import pyxel
import sprite

# Appクラス
class App:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="Hello, Pyxel!!")

        self.w = pyxel.width
        self.h = pyxel.height

        # Sprite
        self.spr = sprite.Sprite(self.w/2, self.h/2, 2, 7)
        
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

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            deg = pyxel.rndi(0, 360)
            self.spr.move(2, deg)


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        self.spr.draw()


# Appクラスを初期化
App()