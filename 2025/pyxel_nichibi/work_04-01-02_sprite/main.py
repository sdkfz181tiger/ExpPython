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

        # TODO: Animation
        self.spr.set_animation("hello", [[0, 0], [8, 0], [16, 0], [24, 0]])
        self.spr.start_animation("hello")
        
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
            #deg = pyxel.rndi(0, 360)
            #self.spr.move(2, deg)
            self.spr.toggle_animation() # Test


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        self.spr.draw()


# Appクラスを初期化
App()