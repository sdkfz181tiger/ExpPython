# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import sprite

W, H = 480, 320 # ゲーム画面の幅と高さ
TITLE = "Hello, Arcade!!" # タイトル

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        self.backgrounds = arcade.SpriteList()
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = W/2
        bkg.center_y = H/2
        self.backgrounds.append(bkg)

        # プレイヤーリストを用意する
        self.players = arcade.SpriteList()

        # プレイヤースプライトを作る
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=W/2, y=H/2)

        self.players.append(self.player) # プレイヤーリストに追加する

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):
        self.players.update() # プレイヤーリストを更新

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw() # プレイヤーリストを描画

def main():
    """ メイン処理 """

    # Window
    window = arcade.Window(W, H, TITLE)

    # GameView
    game = GameView()

    # Show
    window.show_view(game)

    # Run
    arcade.run()

if __name__ == "__main__":
    main()