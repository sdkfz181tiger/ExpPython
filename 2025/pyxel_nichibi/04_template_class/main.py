import pyxel


# Appクラス
class App:

    def __init__(self):
        """ コンストラクタ """
        pyxel.init(80, 60, title="HELLO PYXEL!!")
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """
        pass


    def draw(self):
        """ 描画処理 """
        pyxel.cls(1)


# Appクラスを初期化
App()