import pyxel


# Appクラス
class App:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="HELLO PYXEL!!")

        self.cx = pyxel.width / 2
        self.cy = pyxel.height / 2
        self.counter = 0

        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.counter += 1


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        pyxel.text(self.cx, self.cy, str(self.counter), 7)


# Appクラスを初期化
App()