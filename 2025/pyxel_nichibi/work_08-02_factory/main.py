import pyxel
import pytweening as tween
import utility

# Gameクラス
class Game:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(120, 90, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        self.w = pyxel.width
        self.h = pyxel.height

        # Sprite
        self.spr_a = self.create_slime(self.w/2 - 8, self.h/2, 0, 16, "blue")
        self.spr_b = self.create_slime(self.w/2 + 8, self.h/2, 0, 56, "red")
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        self.spr_a.update()
        self.spr_b.update()

        # WASD
        if pyxel.btnp(pyxel.KEY_W):
            self.spr_a.move(2, 270)
            self.spr_b.move(2, 270)
            self.spr_a.start_animation("up")
            self.spr_b.start_animation("up")
        if pyxel.btnp(pyxel.KEY_A):
            self.spr_a.move(2, 180)
            self.spr_b.move(2, 180)
            self.spr_a.start_animation("left")
            self.spr_b.start_animation("left")
        if pyxel.btnp(pyxel.KEY_S):
            self.spr_a.move(2, 90)
            self.spr_b.move(2, 90)
            self.spr_a.start_animation("down")
            self.spr_b.start_animation("down")
        if pyxel.btnp(pyxel.KEY_D):
            self.spr_a.move(2, 0)
            self.spr_b.move(2, 0)
            self.spr_a.start_animation("right")
            self.spr_b.start_animation("right")


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)
        self.spr_a.draw()
        self.spr_b.draw()

        # マウス座標
        m_x = pyxel.mouse_x
        m_y = pyxel.mouse_y
        pyxel.circ(m_x, m_y, 1, 7)


    def create_slime(self, x, y, u, v, tag=None):
        spr = utility.BaseSprite(x, y, u, v, 8, 8)

        # Animation
        spr.set_animation("down", [[u+8, v], [u+8, v], [u+16, v], [u+24, v]])
        spr.set_animation("up", [[u+8, v+8], [u+8, v+8], [u+16, v+8], [u+24, v+8]])
        spr.set_animation("right", [[u+8, v+16], [u+8, v+16], [u+16, v+16], [u+24, v+16]])
        spr.set_animation("left", [[u+8, v+24], [u+8, v+24], [u+16, v+24], [u+24, v+24]])
        spr.set_animation("dead", [[u+8, v+32], [u+8, v+32], [u+16, v+32], [u+24, v+32], None])
        spr.start_animation("down")

        # Tag
        spr.tag = tag

        return spr


# Gameクラスを初期化
Game()