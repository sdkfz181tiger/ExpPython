import pyxel
import pytweening as tween
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
        self.spr.start_animation("down")
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        self.spr.update()

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            m_x = pyxel.mouse_x
            m_y = pyxel.mouse_y
            self.spr.move_to(m_x, m_y, 1, tween.iterLinear)
            #self.spr.move_to(m_x, m_y, 1, tween.iterEaseOutQuart)
            #self.spr.move_to(m_x, m_y, 1, tween.iterEaseInQuart)

        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            self.spr.stop()


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        self.spr.draw()

        # マウス座標
        m_x = pyxel.mouse_x
        m_y = pyxel.mouse_y
        pyxel.circ(m_x, m_y, 1, 7)


# Appクラスを初期化
App()