# coding: utf-8

"""
デコレータ
"""

#==========
# Main

from random import random
from retrying import retry
from dataclasses import dataclass

#==========
# retryデコレーターを使う

@retry
def my_func1():
    rdm = random()
    if rdm < 0.1:
        print(f"0.1未満です: {rdm}")
    else:
        print(f"raise ValueError: {rdm}")
        raise ValueError(f"エラーです")

# retryデコレーター(繰り返し回数を指定)
@retry(stop_max_attempt_number=30)
def my_func2():
    rdm = random()
    if rdm < 0.1:
        print(f"0.1未満です: {rdm}")
    else:
        print(f"raise ValueError: {rdm}")
        raise ValueError(f"エラーです")

# retryデコレーターが繰り返し実行してくれる
my_func1()

# raise ValueError: 0.49824282636983863
# raise ValueError: 0.7272677155886424
# 0.1未満です: 0.06391566099778068

# 指定回数だけ繰り返したい場合
my_func2()
# 上の結果と同じ

#==========
# dataclassデコレーターを使う

# 値の変更が可能
@dataclass
class Member:
    name: str
    hp: int
    mp: int
    gold: int

member = Member("yusha", 100, 30, 20)
member.gold = 1000# データの変更が可能
print(f"{member.name}, {member.hp}, {member.mp}, {member.gold}")

# 値の変更不可能
@dataclass(frozen=True)
class Enemy:
    name: str
    hp: int
    mp: int
    gold: int

enemy = Enemy("mao", 500, 400, 10)
#enemy.gold = 1000# データの変更は不可能
print(f"{enemy.name}, {enemy.hp}, {enemy.mp}, {enemy.gold}")

#==========
# デコレーターを作成し利用する

# 高階関数: 関数を受け取り、関数を返す事ができる関数の事

# デコレーターを作る
def my_decorator(func):
    def wrapper():# ラッパー関数
        print(f"function: {func.__name__} の前に実行してみる")
        func()# 渡された関数を実行
        print(f"function: {func.__name__} の後に実行してみる")
    return wrapper # ラッパー関数を返す

# デコレーターを利用する
@my_decorator
def my_func():
    print(f"Hello, my_func!!")

# 実行と結果
my_func()
# function: my_func の前に実行してみる
# Hello, my_func!!
# function: my_func の後に実行してみる

# 次の書き方と同義(@my_decoratorを外してテストしてね)
#my_decorator(my_func)()

#==========
# functools.wrapsを利用する

# @wrapsデコレーターを使う事で、
# __name__や、__doc__が上書きされるのを防ぐ

from functools import wraps

def my_decorator(func):
    @wraps(func)# これだけでOK!!
    def wrapper(a):
        """wrap_functionのドキュメントです"""
        func(a)
    return wrapper

@my_decorator
def my_greeting(name):
    """my_greetingのドキュメントです"""
    print(f"こんにちは、{name}さん")

# テスト(成功)
# __name__や、__doc__が上書きされていない
# @wrapsが無い場合はwrapperの方が表示されてしまう
print(my_greeting.__name__)
# my_greeting

print(my_greeting.__doc__)
# my_greetingのドキュメントです