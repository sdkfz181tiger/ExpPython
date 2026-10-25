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

        # Button
        self.btn_a = utility.Button(10, 10, "BTN_A", self.on_click, 5)
        self.btn_b = utility.Button(48, 10, "BTN_B", self.on_click, 8)

        # Counter
        self.counter = 0
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        # Button
        self.btn_a.update()
        self.btn_b.update()

        # Pause
        if self.pause == True:
            return


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        mx = pyxel.mouse_x
        my = pyxel.mouse_y

        # Button
        self.btn_a.draw()
        self.btn_b.draw()

        # Counter
        pyxel.text(self.w/2, self.h/2, str(self.counter), 7)

        # Mouse
        pyxel.rect(mx, my, 1, 1, 7)
        

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

    def on_click(self, title):
        print(f"on_click: {title}")

        if title == "BTN_A":
            self.counter += 1

        if title == "BTN_B":
            self.counter -= 1


# Gameクラスを初期化
Game()