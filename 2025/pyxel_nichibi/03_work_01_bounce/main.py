import pyxel


# Appクラス
class App:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="Hello, Pyxel!!")

        self.w = pyxel.width # 画面横幅
        self.x = 0 # x座標
        self.vx = 1 # x速度

        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """
        self.x += self.vx

        if self.w < self.x:
            self.x = self.w
            self.vx *= -1

        if self.x < 0:
            self.x = 0
            self.vx *= -1


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        pyxel.circ(self.x, 10, 1, 7)


# Appクラスを初期化
App()