import pyxel
import pytweening as tween
import utility

# ゲーム画面
W, H = 120, 90

# ゲームモード
MODE_TITLE = "title"
MODE_PLAY = "play"
MODE_RESULT = "result"

# Gameクラス
class Game:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        self.w = pyxel.width
        self.h = pyxel.height
        self.mode = MODE_TITLE # Mode
        self.score = 0 # Score

        # Sprite
        self.player = utility.BaseSprite(
            self.w/2, self.h/2, 0, 16, 8, 8)
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        if self.mode == MODE_TITLE:
            self.update_title()
            return

        if self.mode == MODE_PLAY:
            self.update_play()
            return

        if self.mode == MODE_RESULT:
            self.update_result()
            return


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # マウス座標
        m_x = pyxel.mouse_x
        m_y = pyxel.mouse_y
        pyxel.circ(m_x, m_y, 1, 7)

        # Score
        pyxel.text(5, 5, f"SCORE:{self.score}", 7)
        self.player.draw()

        if self.mode == MODE_TITLE:
            self.draw_title()
            return

        if self.mode == MODE_PLAY:
            self.draw_play()
            return

        if self.mode == MODE_RESULT:
            self.draw_result()
            return


    def reset(self):
        """ Reset """
        self.score = 0
        self.player.x = self.w / 2
        self.player.y = self.h / 2


    def update_title(self):
        """ update(title) """
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.mode = MODE_PLAY

        self.player.update()


    def update_play(self):
        """ update(play) """

        self.score += 1
        if 100 <= self.score:
            self.mode = MODE_RESULT

        self.player.update()


    def update_result(self):
        """ update(result) """
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.mode = MODE_TITLE
            self.reset() # Reset

        self.player.update()


    def draw_title(self):
        """ draw(title) """
        pyxel.text(5, self.h-10, "TITLE", 7)


    def draw_play(self):
        """ draw(play) """
        pyxel.text(5, self.h-10, "PLAY", 7)


    def draw_result(self):
        """ draw(result) """
        pyxel.text(5, self.h-10, "GAME OVER!!", 7)


# Gameクラスを初期化
Game()