# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import src.sprite as sprite
import src.result as result
import src.utility as utility

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.background_color = arcade.color.PAYNE_GREY

        # Wait
        self.view_wait_time = 0.5
        self.view_finish_flg = False

        # 背景スプライト
        self.backgrounds = arcade.SpriteList()
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = window.width/2
        bkg.center_y = window.height/2
        self.backgrounds.append(bkg)

        # プレイヤースプライト
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=window.width/2, 
                                    y=window.height/2)
        self.players.append(self.player)

        # 小判スプライト
        self.coins = arcade.SpriteList()
        for i in range(3):
            x = random.random() * window.width
            y = random.random() * window.height
            coin = sprite.Coin("images/coin/coin_01.png",
                               x=x, y=y)
            self.coins.append(coin)

        # スコア
        self.score = 0
        self.score_text = arcade.Text(
            "SCORE: {}".format(self.score), 
            window.width/2, window.height-20,
            arcade.color.BLACK, 12,
            anchor_x="center", anchor_y="top")

        # サウンドオブジェクト
        self.se_coin = arcade.Sound("sounds/se_coin.ogg")

    def on_key_press(self, key, key_modifiers):
        if 0.0 < self.view_wait_time: return # Wait

        # Move(WASD)
        if key == arcade.key.W: self.player.move(90, 90, "back")
        if key == arcade.key.A: self.player.move(90, 180, "left")
        if key == arcade.key.S: self.player.move(90, 270, "front")
        if key == arcade.key.D: self.player.move(90, 0, "right")

    def on_key_release(self, key, key_modifiers):
        if 0.0 < self.view_wait_time: return # Wait
        self.player.stop()

    def on_update(self, delta_time):
        if 0.0 < self.view_wait_time: self.view_wait_time -= delta_time # Wait

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
        # Finish or Not
        if not self.view_finish_flg:
            if not self.coins:
                self.view_wait_time = 2.0
                self.view_finish_flg = True
                self.player.stop()
                self.player.change_animation("front")
            return
        # Finish to Result
        if 0.0 < self.view_wait_time: return
        self.window.show_view(result.ResultView(self.window)) # ResultView