import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

w = pyxel.width
h = pyxel.height

def draw_character(x, y):
    pyxel.circb(x, y, 12, 7)
    pyxel.rect(x-5, y-4, 4, 4, 7)
    pyxel.rect(x-3, y-2, 2, 2, 2)
    pyxel.rect(x+2, y-4, 4, 4, 7)
    pyxel.rect(x+4, y-2, 2, 2, 2)
    pyxel.circb(x, y+2, 2, 7)
    pyxel.line(x-4, y+7, x+4, y+7, 7)

draw_character(w/2-20, h/2)
draw_character(w/2+20, h/2)

# 画面表示
pyxel.show()