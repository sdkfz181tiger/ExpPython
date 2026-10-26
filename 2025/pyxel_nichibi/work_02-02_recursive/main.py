import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

w = pyxel.width
h = pyxel.height

def draw_circles(x, y, n):
    if 4 <= n:
        return
    size = n * 4
    pyxel.circb(x, y, size, 7)
    draw_circles(x, y, n+1)
    
draw_circles(w/2-30, h/2-20, 1)
draw_circles(w/2+20, h/2+20, 1)

# 画面表示
pyxel.show()