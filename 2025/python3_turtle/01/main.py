# coding: utf-8

"""
かじるプログラミング_turtle

Install
    $ brew install python-tk
"""

import turtle

def draw_square(ttl, line_len):
    """ 四角形 """
    ttl.forward(line_len)
    ttl.right(90)
    ttl.forward(line_len)
    ttl.right(90)
    ttl.forward(line_len)
    ttl.right(90)
    ttl.forward(line_len)

def draw_triangle(ttl, line_len):
    """ 三角形 """
    ttl.forward(line_len)
    ttl.right(120)
    ttl.forward(line_len)
    ttl.right(120)
    ttl.forward(line_len)

def draw_hexagon(ttl, line_len):
    """ 六角形 """
    for i in range(6):
        ttl.forward(line_len)
        ttl.right(60)

def draw_octagon(ttl, line_len):
    """ 八角形 """
    for i in range(8):
        ttl.forward(line_len)
        ttl.right(45)

def draw_anything(ttl, line_len, turn_deg, turn_times):
    """ x角形 """
    for i in range(turn_times):
        ttl.forward(line_len)
        ttl.right(turn_deg)

def draw_spiral(ttl, line_len):
    """ 四角渦巻き """
    if 400 < line_len: return
    ttl.forward(line_len)
    ttl.right(90)
    draw_spiral(ttl, line_len+5)

def main():
    """ メイン処理 """
    
    # Turtle
    turtle.setup(width=480, height=320)
    screen = turtle.Screen()
    ttl = turtle.Turtle()
    #draw_square(ttl, 50)
    #draw_triangle(ttl, 50)
    #draw_hexagon(ttl, 50)
    #draw_octagon(ttl, 50)
    draw_anything(ttl, 50, 45, 8)
    screen.exitonclick()

if __name__ == "__main__":
    main()