# coding: utf-8

"""
正方形を表すクラス
"""

#==========
# Main

# 長方形クラス
class Rectangle():

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calc_perimeter(self):
        return self.width * 2 + self.height * 2

    def calc_area(self):
        return self.width * self.height

    def __str__(self):
        return f'w:{self.width}, h:{self.height}'

# 正方形
class Square(Rectangle):

    def __init__(self, w):
        super().__init__(w, w)

def main():

    # Test
    square = Square(100)
    print(square)
    print(square.calc_perimeter())
    print(square.calc_area())

if __name__ == "__main__":
    main()
