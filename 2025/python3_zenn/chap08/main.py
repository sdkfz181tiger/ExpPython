# coding: utf-8

"""
Python3_Zenn
"""

class User:
    """ クラスの定義 """
    def __init__(self, nick_name, real_name):
        """ 初期化処理 """
        self.nick_name = nick_name # インスタンス変数
        self.real_name = real_name # インスタンス変数

    def greeting(self):
        """ インスタンスメソッド """
        print(f"{self.nick_name}の本名は、{self.real_name}だよ!!")

    def say_something(self, word):
        """ インスタンスメソッド """
        print(f"{self.nick_name}「{word}」")


user1 = User("まる子", "さくらももこ") # インスタンス化
user1.greeting() # メソッドの実行
user1.say_something("うぅ〜ん、いけずぅ〜") # メソッドの実行
# まる子の本名は、さくらももこだよ!!
# まる子「うぅ〜ん、いけずぅ〜」

user2 = User("たまちゃん", "穂波たまえ") # インスタンス化
user2.greeting() # メソッドの実行
user2.say_something("まるちゃん...") # メソッドの実行
# たまちゃんの本名は、穂波たまえだよ!!
# たまちゃん「まるちゃん...」

user3 = User("丸尾くん", "丸尾末尾") # インスタンス化
user3.greeting() # メソッドの実行
user3.say_something("ズバリ、皆殺しでしょう!!") # メソッドの実行
# 丸尾くんの本名は、丸尾末尾だよ!!
# 丸尾くん「ズバリ、皆殺しでしょう!!」