# coding: utf-8

"""
doctestモジュール
"""

#==========
# Main

import doctest

if __name__ == "__main__":
    doctest.testfile("doctest.txt")# doctestを実行

"""
Run
$python3 main.py -v

File "/Users/xxx(省略)
Failed example:
    div(6, 2)
Expected:
    4.0
Got:
    3.0
**********************
1 items had failures:
   1 of   2 in doctest.txt
***Test Failed*** 1 failures.
"""