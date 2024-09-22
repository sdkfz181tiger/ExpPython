# coding: utf-8

"""
secretsモジュール
"""

#==========
# Main

import random, secrets, string
from urllib import parse

#==========
# ランダムで文字を選ぶ

# 英字+数字
alpha_num = string.ascii_letters + string.digits
print(alpha_num)

# 英字+数字からランダムで8文字選ぶ
password = "".join(secrets.choice(alpha_num) for i in range(8))
print(password)

#==========
# トークンの生成(引数はトークンサイズ)
print(secrets.token_bytes(8))# バイト列
# b'\xd7)\xb4\x1f\xcf0\xf1\xae'

print(secrets.token_hex(8))# 16進数
# 6b9870784b136bff

print(secrets.token_urlsafe(8))# URL用テキスト(Base64)
# NLiIK-A81g4

#==========
# トークンの生成と比較

# 1, トークンの生成
token = secrets.token_urlsafe(8)
print(f"token: {token}")
# token: Gp_Kq8wOhLc

# 2, トークンをURLに設定する
url = f"https://hoge.com/?reset={token}"
parsed = parse.urlparse(url)
query = parse.parse_qs(parsed.query)
print(f"reset: {query["reset"][0]}")
# reset: Gp_Kq8wOhLc

# 3, 元のトークンと、URLからのトークンを比較する
print(secrets.compare_digest(token, query["reset"][0]))
# True

#==========
# 10文字のパスワードを生成
# 英字、数字、記号をそれぞれ1文字以上含む

# 1, 英字を配列に
letters = [i for i in string.ascii_letters]
random.shuffle(letters)
#print(letters)

# 2, 数字を配列に
digits = [i for i in string.digits]
random.shuffle(digits)
#print(digits)

# 3, 記号を配列に
puncs = [i for i in string.punctuation]
random.shuffle(puncs)
#print(puncs)

# 4, 3つの要素数を確定
len_pass = 10# パスワード文字数
nums = [i+1 for i in range(len_pass-1)]
random.shuffle(nums)
thres = sorted(nums[:2])# 文字、数字、記号の境界
print(thres)

# 5, 3つの要素数分だけ英字、数字、記号から抜き出し連結
letters = letters[0:thres[0]]
digits = digits[0:thres[1]-thres[0]]
puncs = puncs[0:len_pass-thres[1]]

# 6, 3つの配列を連結しシャッフル
arr = letters
arr += digits
arr += puncs
random.shuffle(arr)
password = "".join(arr)
print(password)
# s$efK{\`U3
