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

# parse
parsed = parse.parse_qs(result.query)
print(parsed)
# {'hoge': ['xxx'], 'fuga': ['xxx']}

# urlencode(要素に配列がある場合)
query = {"key1": "a", "key2": ["b", "c"]}

encoded1 = parse.urlencode(query)
print(encoded1)
# key1=a&key2=%5B%27b%27%2C+%27c%27%5D

encoded2 = parse.urlencode(query, doseq=True)
print(encoded2)
# key1=a&key2=b&key2=c

# urlencode(要素が空白の場合)
query = {"key1": " "}

encoded1 = parse.urlencode(query)
print(encoded1)
# key1=+

encoded2 = parse.urlencode(query, quote_via=parse.quote)
print(encoded2)
# key1=%20

# quote関数(空白を%20にエンコード)
print(parse.quote(url))

# quote_plus関数(空白を+にエンコード)
print(parse.quote_plus(url))

# join
print(parse.urljoin("https://www.xxx.com", "/yyy/zzz"))
# https://www.xxx.com/yyy/zzz
