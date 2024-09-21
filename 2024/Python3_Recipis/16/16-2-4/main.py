# coding: utf-8

"""
unittestモジュール
"""

#==========
# Main

import unittest

class SetUpAndSetUpClassTest(unittest.TestCase):

    def setUp(self):
        print("setUp!!")

    @classmethod
    def setUpClass(clz):
        print("setUpClass!!")

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

setUpClass!!
setUp!!
test_hop!!
.setUp!!
test_jump!!
.setUp!!
test_step!!
.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
"""