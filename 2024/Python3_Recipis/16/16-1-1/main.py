# coding: utf-8

"""
doctestモジュール
"""

#==========
# Main

import doctest

def div(a, b):
    """
    答えは小数で返す

    >>> [div(n, 2) for n in range(5)]
    [0.0, 0.5, 1.0, 1.5, 2.0]
    """

    return a / b

if __name__ == "__main__":
    doctest.testmod()# doctestを実行

"""
Run
$python3 main.py -v

Trying:
    [div(n, 2) for n in range(5)]
Expecting:
    [0.0, 0.5, 1.0, 1.5, 2.0]
ok
1 items had no tests:
    __main__
1 items passed all tests:
   1 tests in __main__.div
1 tests in 2 items.
1 passed and 0 failed.
Test passed.
"""