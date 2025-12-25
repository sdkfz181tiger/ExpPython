# coding: utf-8

"""
Python3認定基礎試験サンプルコード
"""

# def

def helloFunc():
    """ 最小の関数 """
    pass

def fib1(num):
    """ numまでのフィボナッチ数を書き出す """
    a, b = 0, 1
    while(a < num):
        print(a)
        a, b = b, a + b

fib1(5)

def fib2(num):
    """ numまでのフィボナッチ数をリストに格納する """
    a, b = 0, 1
    data = []
    while(a < num):
        data.append(a)
        a, b = b, a + b
    return data

print(fib2(30))

# キーワード引数
def jotaro_says(who_a, who_b="俺", emotion="怒らせ"):
    print(who_a + "は、" + who_b + "を" + emotion + "た")

jotaro_says("てめー")
jotaro_says("てめー", "花京院")
jotaro_says("てめー", "花京院", "笑わせ")
jotaro_says("てめー", emotion="泣かせ", who_b="ポルナレフ")
jotaro_says("てめー", emotion="哀しませ", who_b="ジョセフ")


# 可変長引数と可変長キーワード引数
def jojo_dialogue(title, *quotes, **info):
    """ * 可変長位置引数, ** 可変長キーワード引数 """
    print("===", title, "===")
    print("-" * 40)

    print("[名台詞]")
    for q in quotes:
        print(" -", q)

    print("-" * 40)
    print("[補足情報]")
    for key in info:
        print(f"{key}:{info[key]}")

jojo_dialogue(
    "DIOの名台詞",
    "マヌケが・・・・・",
    "知るがいい・・・・・",
    "「世界（ザ・ワールド）」の真の能力は・・・",
    "まさに!「世界を支配する」能力だということを!",
    "「世界（ザ・ワールド）」!!",
    staring = "DIO",
    stand = "THE WORLD",
    location = "カイロの屋敷"
)



