# coding: utf-8

"""
かじるプログラミング_turtle

Install
    $ brew install python-tk
"""

import turtle

def draw_5_star(ttl, line_len):
    """ 5星形 """
    for i in range(5):
        ttl.forward(line_len)
        ttl.right(144)

def draw_n_star(ttl, line_len, n):
    """ n星形 """
    deg = 180 - (360 / n)
    for i in range(n):
        ttl.forward(line_len)
        ttl.right(deg)

def main():
    """ メイン処理 """
    
    # Turtle
    turtle.setup(width=480, height=320)
    screen = turtle.Screen()
    ttl = turtle.Turtle()
    #draw_5_star(ttl, 50)
    draw_n_star(ttl, 100, 5)
    screen.exitonclick()

if __name__ == "__main__":
    main()