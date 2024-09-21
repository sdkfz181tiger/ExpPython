# coding: utf-8

"""
unittestモジュール
"""

#==========
# Main

import unittest

class TearDownAndTearDownClassTest(unittest.TestCase):

    def tearDown(self):
        print("tearDown!!")

    @classmethod
    def tearDownClass(clz):
        print("tearDownClass!!")

    def test_hop(self):
        print("test_hop!!")

    def test_step(self):
        print("test_step!!")

    def test_jump(self):
        print("test_jump!!")

if __name__ == "__main__":
    unittest.main()# テストを実行する

"""
Run
$python3 main.py

test_hop!!
tearDown!!
.test_jump!!
tearDown!!
.test_step!!
tearDown!!
.tearDownClass!!

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
"""