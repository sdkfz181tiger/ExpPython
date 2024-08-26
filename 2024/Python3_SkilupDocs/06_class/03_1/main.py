# coding: utf-8

"""
寿司を表すクラス
"""

#==========
# Main

# 基底クラス
class Nigiri():

    def __init__(self, top=None, price=100, wasabi=False):
        self.top = top
        self.price = price
        self.wasabi = wasabi

    def __str__(self):
        return f'top:{self.top}, price:{self.price}, wasabi:{self.wasabi}'

# まぐろ
class Maguro(Nigiri):

    def __init__(self, wasabi=False):
        super().__init__("まぐろ", 220, wasabi)

# かつお
class Katsuo(Nigiri):

    def __init__(self, wasabi=False):
        super().__init__("かつお", 180, wasabi)

# いくら
class Ikura(Nigiri):

    def __init__(self, wasabi=False):
        super().__init__("いくら", 200, wasabi)

def main():

    # Test
    maguro = Maguro()
    print(maguro)

    katsuo = Katsuo()
    print(katsuo)

    ikura = Ikura()
    print(ikura)

if __name__ == "__main__":
    main()
