import pyxel


# Gameクラス
class Game:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="HELLO PYXEL!!")
        pyxel.load("my_resource.pyxres")

        self.x = 0
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """
        print(f"xは,{self.x}")
        self.x += 1


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        pyxel.circ(self.x, 10, 3, 7)


# Gameクラスを初期化
Game()