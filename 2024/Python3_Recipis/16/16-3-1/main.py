# coding: utf-8

"""
unittest.mockモジュール
"""

#==========
# Main

from unittest.mock import MagicMock
from api_shopping import ShoppingAPI

# テスト対象のクラス
api = ShoppingAPI()

# テスト対象の関数をMagicMockで上書き
api.get_items = MagicMock()
print(api.get_items)# 上書きを確認
# <MagicMock id='4493138336'>

# テスト対象の関数の戻り値を設定する
api.get_items.return_value = ["モック1", "モック2", "モック3"]
print(api.get_items("商品1"))
# ['モック1', 'モック2', 'モック3']

# テスト対象の関数に例外を設定できる
api.get_items.side_effect = Exception("例外を設定します")
print(api.get_items("商品1"))
# Traceback (most recent call last):
# ...(省略)
# Exception: 例外を設定します

