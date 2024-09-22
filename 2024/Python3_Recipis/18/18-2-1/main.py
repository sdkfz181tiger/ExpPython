# coding: utf-8

"""
hashlibモジュール
"""

#==========
# Main

import hashlib

# 利用可能なハッシュ関数
print(hashlib.algorithms_available)
# {'ripemd160', 'sha384', 'sha512', 'sha3_256', ...(以下略)}

# sha512
print(hashlib.sha512(b"Hello, hashlib!!").hexdigest())
# ec3fcf998b9f8823824e69ade572...(以下略)

# sha384
print(hashlib.sha384(b"Hello, hashlib!!").hexdigest())
# 58a931d8269d66084a8bc824967e...(以下略)

# sha256
print(hashlib.sha256(b"Hello, hashlib!!").hexdigest())
# 55dd59f6667894e79bbbe16233ce...(以下略)

#==========
# 安全なパスワードハッシュの生成

algorithm = "sha256"# アルゴリズム
password = b"Your secret password!!"# ハッシュ化対象
salt = b"Your secret salt!!"# ソルト
iteration = 1000# ストレッチング回数(推奨値:100000)

# ハッシュ処理
h_password = hashlib.pbkdf2_hmac(algorithm, password, salt, iteration).hex()
print(h_password)
# 55dd59f6667894e79bbbe16233ce...(以下略)
