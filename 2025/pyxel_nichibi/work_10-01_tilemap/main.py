import pyxel
import pytweening as tween
import utility

# ゲーム画面
W, H = 120, 90

# カメラ
CAMERA_AREA_W  = 192
CAMERA_AREA_H  = 192
CAMERA_PAD_X   = 40
CAMERA_PAD_Y   = 40
CAMERA_LIMIT_L = W - CAMERA_AREA_W
CAMERA_LIMIT_R = 0
CAMERA_LIMIT_T = H - CAMERA_AREA_H
CAMERA_LIMIT_B = 0


# Gameクラス
class Game:

    def __init__(self):
        """ コンストラクタ """
        # Pyxel初期化
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        self.w = pyxel.width
        self.h = pyxel.height

        # Camera
        self.camera_x = 0
        self.camera_y = 0

        # Sprite
        self.player = utility.BaseSprite(32, 32, 0, 16, 8, 8)
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        # Collision x Gate x Coin
        self.player.update()
        utility.collide_tile(self.player, utility.TILE_GATE)
        if utility.collide_tile(self.player, utility.TILE_COIN, (0, 0)):
            pyxel.play(0, 0)   
        
        # WASD
        if pyxel.btnp(pyxel.KEY_W):
            self.player.move(2, 270)

        if pyxel.btnp(pyxel.KEY_A):
            self.player.move(2, 180)

        if pyxel.btnp(pyxel.KEY_S):
            self.player.move(2, 90)
        
        if pyxel.btnp(pyxel.KEY_D):
            self.player.move(2, 0)

        if pyxel.btnr(pyxel.KEY_W) or pyxel.btnr(pyxel.KEY_A):
            self.player.stop()

        if pyxel.btnr(pyxel.KEY_S) or pyxel.btnr(pyxel.KEY_D):
            self.player.stop()


    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        self.camera_on()

        # Tilemap
        pyxel.bltm(0, 0, 0, 0, 0, 
                   CAMERA_AREA_W, CAMERA_AREA_H, 0)

        self.player.draw()

        self.camera_off()

        # マウス座標
        m_x = pyxel.mouse_x
        m_y = pyxel.mouse_y
        pyxel.circ(m_x, m_y, 1, 7)


    def camera_on(self):

        line_l = 0 - self.camera_x + CAMERA_PAD_X
        if self.player.x < line_l:
            self.camera_x += line_l - self.player.x
            if CAMERA_LIMIT_R < self.camera_x:
                self.camera_x = CAMERA_LIMIT_R

        line_r = W - self.camera_x - CAMERA_PAD_X
        if line_r < self.player.x:
            self.camera_x += line_r - self.player.x
            if self.camera_x < CAMERA_LIMIT_L:
                self.camera_x = CAMERA_LIMIT_L

        line_t = 0 - self.camera_y + CAMERA_PAD_Y
        if self.player.y < line_t:
            self.camera_y += line_t - self.player.y
            if CAMERA_LIMIT_B < self.camera_y:
                self.camera_y = CAMERA_LIMIT_B

        line_b = H - self.camera_y - CAMERA_PAD_Y
        if line_b < self.player.y:
            self.camera_y += line_b - self.player.y
            if self.camera_y < CAMERA_LIMIT_T:
                self.camera_y = CAMERA_LIMIT_T

        pyxel.camera(-self.camera_x, -self.camera_y)


    def camera_off(self):
        pyxel.camera()


# Gameクラスを初期化
Game()