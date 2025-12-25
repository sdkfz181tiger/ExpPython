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
        self.w = self.window.width
        self.h = self.window.height

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # 背景スプライト
        self.backgrounds = arcade.SpriteList()
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = self.w / 2
        bkg.center_y = self.h / 2
        self.backgrounds.append(bkg)

        # プレイヤースプライト
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=self.w/2, y=self.h/2)
        self.players.append(self.player)

    def on_key_press(self, key, key_modifiers):
        # Move(WASD)
        if key == arcade.key.W: self.player.move(90, 90) # 上へ
        if key == arcade.key.A: self.player.move(90, 180) # 左へ
        if key == arcade.key.S: self.player.move(90, 270) # 下へ
        if key == arcade.key.D: self.player.move(90, 0) # 右へ

    def on_key_release(self, key, key_modifiers):
        self.player.stop() # 停止

    def on_update(self, delta_time):
        self.players.update(delta_time)

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw()

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    game = GameView(window)
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()