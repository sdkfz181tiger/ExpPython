# coding: utf-8

"""
urllibモジュール(parse)
"""

#==========
# Main

from urllib import parse

url = "https://www.xxx.com/yyy/zzz/?key1=a&key2=b"

# parse
result = parse.urlparse(url)
print(result)
# ParseResult(scheme='https', netloc='xxx', path='xxx', 
#                   params='', query='xxx', fragment='')

print(result.geturl())
# https://xxx.yyy.ne.jp/...

print(result[0])
# https

print(result.scheme)
# https

print(result.hostname)
# xxx.yyy.ne.jp

#==========
# query文字列 -> 配列/リストへ

# parse(queryを連想配列に)
parsed = parse.parse_qs(result.query)
print(parsed)
# {'hoge': ['xxx'], 'fuga': ['xxx']}

# parse(queryをタプルのリストに)
parsed = parse.parse_qsl(result.query)
print(parsed)
# [('key1', 'a'), ('key2', 'b')]

#==========
# 配列/リスト -> query文字列へ

# urlencode(要素に配列がある場合)
data = {"key1": "a", "key2": ["b", "c"]}

# 一つの文字列として並べる
encoded = parse.urlencode(data)
print(encoded)
# key1=a&key2=%5B%27b%27%2C+%27c%27%5D

# 同一のキーにして並べる
encoded = parse.urlencode(data, doseq=True)
print(encoded)
# key1=a&key2=b&key2=c

#==========
# urlencode(要素が空白の場合)
query = {"key1": " "}

# +として置き換える
encoded = parse.urlencode(query)
print(encoded)
# key1=+

# %20に置き換える
encoded = parse.urlencode(query, quote_via=parse.quote)
print(encoded)
# key1=%20

#==========
# 文字列をパーセントエンコード

# quote関数(空白を%20にエンコード)
print(parse.quote(url))
# https%3A//www.xxx.com/yyy/zzz/%3Fkey1%3Da%26key2%3Db

# quote_plus関数(空白を+にエンコード)
print(parse.quote_plus(url))
# https%3A%2F%2Fwww.xxx.com%2Fyyy%2Fzzz%2F%3Fkey1%3Da%26key2%3Db

#==========
# URLを結合

# join
print(parse.urljoin("https://www.xxx.com", "/yyy/zzz"))
# https://www.xxx.com/yyy/zzz
