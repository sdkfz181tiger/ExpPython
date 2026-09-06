# coding: utf-8

"""
1, Install
    $ python3 -m pip install py5
"""

import py5

def main():
    """ Main """
    print("main!!")
    py5.run_sketch()# Py5

def setup():
    py5.size(200, 200)
    py5.rect_mode(py5.CENTER)

def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)

if __name__ == "__main__":
    main()