# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import sprite
import random

W, H = 480, 320
TITLE = "Hello, Arcade!!"
window = None

# Title
class TitleView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.PAYNE_GREY

        # Message
        self.msg_info = arcade.Text(
            "SPACE TO GAME", 
            W/2, H-20, arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Space to Game
        if key == arcade.key.SPACE: 
            window.show_view(GameView()) # GameView

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.msg_info.draw()

# Game
class GameView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.PAYNE_GREY

        # Wait
        self.wait_time = 0.5
        self.finish_flg = False

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

        # 小判スプライト
        self.coins = arcade.SpriteList()
        for i in range(4):
            x = random.random() * W
            y = random.random() * H
            coin = sprite.Coin("images/coin/coin_01.png",
                               x=x, y=y)
            self.coins.append(coin)

        # スコア
        self.score = 0
        self.score_text = arcade.Text(
            "SCORE: {}".format(self.score), 
            W/2, H-20, arcade.color.BLACK, 12,
            anchor_x="center", anchor_y="top")

        # サウンドオブジェクト
        self.se_coin = arcade.Sound("sounds/se_coin.ogg")

    def on_key_press(self, key, key_modifiers):
        if 0.0 < self.wait_time: return # Wait

        # Move(WASD)
        if key == arcade.key.W: self.player.move(90, 90, "back")
        if key == arcade.key.A: self.player.move(90, 180, "left")
        if key == arcade.key.S: self.player.move(90, 270, "front")
        if key == arcade.key.D: self.player.move(90, 0, "right")

    def on_key_release(self, key, key_modifiers):
        if 0.0 < self.wait_time: return # Wait
        self.player.stop()

    def on_update(self, delta_time):
        if 0.0 < self.wait_time: self.wait_time -= delta_time # Wait

        self.players.update(delta_time)
        self.coins.update(delta_time)

        # プレイヤー x コインリスト
        hit_coins = arcade.check_for_collision_with_list(self.player,
                                                         self.coins)
        for coin in hit_coins:
            coin.remove_from_sprite_lists()
            # スコア
            self.score += 1
            self.score_text.text = "SCORE: {}".format(self.score)
            # サウンドを再生
            arcade.play_sound(self.se_coin)

        self.check_finish() # Finish or not

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw()
        self.players.draw()
        self.coins.draw()
        self.score_text.draw()

    def check_finish(self):
        # Finish or not
        if not self.finish_flg:
            if not self.coins:
                self.wait_time = 2.0
                self.finish_flg = True
                self.player.stop("front")
            return
        # Result
        if 0.0 < self.wait_time: return
        window.show_view(ResultView()) # ResultView

# Result
class ResultView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.PAYNE_GREY

        # Message
        self.msg_info = arcade.Text(
            "SPACE TO TITLE", 
            W/2, H-20, arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Space to Game
        if key == arcade.key.SPACE: 
            window.show_view(TitleView()) # TitleView

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.msg_info.draw()

def main():
    """ メイン処理 """
    global window
    window = arcade.Window(W, H, TITLE)
    window.show_view(TitleView()) # TitleView
    arcade.run()

if __name__ == "__main__":
    main()