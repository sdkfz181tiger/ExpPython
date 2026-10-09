import pyxel


# Appクラス
class App:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="HELLO PYXEL!!")

        self.x = 0
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """
        self.x += 1


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        pyxel.circ(self.x, 10, 1, 7)


# Appクラスを初期化
App()