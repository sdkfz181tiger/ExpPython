# coding: utf-8

"""
doctestモジュール
"""

#==========
# Main

import doctest

def div(a, b):
    """
    0除算の時は例外を出力する

    >>> div(1, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: divition by zero
    """

    return a / b

if __name__ == "__main__":
    doctest.testmod()# doctestを実行

"""
Run
$python3 main.py -v

File "/Users/xxx(省略)
Failed example:
    div(1, 0)
Expected:
    Traceback (most recent call last):
        ...
    ZeroDivisionError: divition by zero
Got:
    Traceback (most recent call last):
        (省略)
        return a / b
               ~~^~~
    ZeroDivisionError: division by zero
1 items had no tests:
    __main__
*********************
1 items had failures:
   1 of   1 in __main__.div
1 tests in 2 items.
0 passed and 1 failed.
***Test Failed*** 1 failures.
"""