# coding: utf-8

"""
unittestモジュール
"""

#==========
# Main

import unittest
from target import div_ok, div_ng

# TestCaseクラスを継承
class DivTest(unittest.TestCase):
    # test_xxxの名前で関数を用意
    def test_the_div_of_two_integers(self):
        actual = div_ok(6, 3)# テスト対象を実行(正しい結果を返す関数)
        #actual = div_ng(6, 3)# テスト対象を実行(間違えた結果を返す関数)
        expected = 2.0
        self.assertEqual(actual, expected)# 値が等しいか確認

if __name__ == "__main__":
    unittest.main()# テストを実行する

"""
Run
$python3 main.py

div_ok関数の場合(正しい結果を返す関数をテストした場合)
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

div_ng関数の場合(間違った結果を返す関数をテストした場合)
F
======================================================================
FAIL: test_the_div_of_two_integers (__main__.DivTest.test_the_div_of_two_integers)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/xxx(省略)", line 20, in test_the_div_of_two_integers
    self.assertEqual(actual, expected)
AssertionError: 1.0 != 2.0

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
"""