# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import sprite

class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width # ゲーム画面の幅
        self.h = self.window.height # ゲーム画面の高さ

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # 背景スプライト
        self.backgrounds = arcade.SpriteList()
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = self.w / 2
        bkg.center_y = self.h / 2
        self.backgrounds.append(bkg)

        # プレイヤーリストを用意する
        self.players = arcade.SpriteList()

        # プレイヤースプライトを作る
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=self.w/2, y=self.h/2)

        self.players.append(self.player) # プレイヤーリストに追加する

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):
        self.players.update(delta_time) # プレイヤーリストを更新

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw() # プレイヤーリストを描画

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    game = GameView(window)
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()