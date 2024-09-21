# coding: utf-8

"""
unittestモジュール
"""

#==========
# Main

import unittest
from target import div_ok

# 割り算の結果を格納している配列
# 1件目は正しい結果、2件目と3件目は間違った結果を格納
examples = [
    [6, 3, 2.0],
    [6, 2, 5.0],
    [6, 1, 4.0]
]

# TestCaseクラスを継承
class DivTest(unittest.TestCase):
    # test_xxxの名前で関数を用意
    def test_the_div_of_two_integers(self):
        # データを順番に取り出す
        for idx, example in enumerate(examples):
            # 1件づつテストデータを取り出す
            a, b, expected = example
            # subTestの引数にテストデータを渡す
            with self.subTest(f"{a}/{b}={expected}", idx=idx):
                self.assertEqual(div_ok(a, b), expected)# テスト実行(正しい結果を返す関数)

if __name__ == "__main__":
    unittest.main()# テストを実行する

"""
Run
$python3 main.py

FF
======================================================================
FAIL: test_the_div_of_two_integers (__main__.DivTest.test_the_div_of_two_integers) [6/2=5.0] (idx=1)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/xxx(省略)", line 30, in test_the_div_of_two_integers
    self.assertEqual(div_ok(a, b), expected)# テスト実行
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 3.0 != 5.0

======================================================================
FAIL: test_the_div_of_two_integers (__main__.DivTest.test_the_div_of_two_integers) [6/1=4.0] (idx=2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/xxx(省略)", line 30, in test_the_div_of_two_integers
    self.assertEqual(div_ok(a, b), expected)# テスト実行
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: 6.0 != 4.0

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=2)
"""