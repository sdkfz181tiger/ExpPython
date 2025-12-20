# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import sprite

W, H = 480, 320
TITLE = "Hello, Arcade!!"

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # 背景スプライト
        self.backgrounds = arcade.SpriteList()
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = W/2
        bkg.center_y = H/2
        self.backgrounds.append(bkg)

        # プレイヤースプライト
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=W/2, y=H/2)
        self.players.append(self.player)

        self.player.move(90, 30) # プレイヤーを移動させてみる

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):
        self.players.update()

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw()

def main():
    """ メイン処理 """
    window = arcade.Window(W, H, TITLE)
    game = GameView()
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()