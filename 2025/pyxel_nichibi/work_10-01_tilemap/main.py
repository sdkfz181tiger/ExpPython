import pyxel
import pytweening as tween
import utility

# タイルの種類
TILE_GATE  = 1
TILE_COIN  = 2
TILE_TYPES = {
    (2, 7): TILE_GATE, # Gate
    (3, 7): TILE_COIN  # Coin
}

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
        self.player = utility.BaseSprite(64, 64, 0, 16, 8, 8)

        # Camera
        self.camera = utility.CameraManager(128, 128)
        self.camera.set_center(self.player)
        
        # Pyxel実行
        pyxel.run(self.update, self.draw)


    def update(self):
        """ 更新処理 """

        # Collision x Gate x Coin
        self.player.update()
        utility.collide_tile(self.player, TILE_GATE, TILE_TYPES)
        if utility.collide_tile(self.player, TILE_COIN, TILE_TYPES, (0, 0)):
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

        # Camera
        self.camera.camera_on(self.player)

        # Tilemap
        pyxel.bltm(0, 0, 0, 0, 0, 
                   self.camera.area_w, 
                   self.camera.area_h, 0)

        self.player.draw()

        self.camera.camera_off()

        # マウス座標
        m_x = pyxel.mouse_x
        m_y = pyxel.mouse_y
        pyxel.circ(m_x, m_y, 1, 7)


# Gameクラスを初期化
Game()