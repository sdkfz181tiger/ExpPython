#!/usr/bin/env python3

"""
簡易Webサーバーの作り方
	1, Webアプリディレクトリ直下にフォルダを用意して配置
		./cgi-bin 
	2, 配置したプログラムに実行権限を付与
		$ chmod +x cgi-bin/main.py
	3, Webサーバーを起動
		$ python3 -m http.server --cgi 8080
	4, ブラウザからアクセス
		localhost:8080/cgi-bin/main.py
"""

import random, cgi, cgitb

# Debug
cgitb.enable()

# Header
print("Content-Type: text/html; charser=utf-8")
print("")

# Random
dice = random.randint(1, 6)

# GETから値を取得する
params = cgi.FieldStorage()
hoge = params.getvalue("hoge", default="none")
fuga = params.getvalue("fuga", default="none")

# HTML
html = """
<!DOCTYPE html>
<html>
<head>
	<meta charset="UTF-8">
	<title>Hello, World!!</title>
</head>
<body>
	<h1>Hello, World!!</h1>
	<p>Dice:{dice}</p>
	<p>Hoge:{hoge}</p>
	<p>Fuga:{fuga}</p>
</body>
</html>
""".format(dice=dice, hoge=hoge, fuga=fuga)
print(html)