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

# GETにhoge,fugaが含まれるかどうか
if (not "hoge" in params) or (not "fuga" in params):
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
		<form>
			<p>Dice:{dice}</p>
			<p>Hoge:<input type="text" name="hoge" value="1"></p>
			<p>Fuga:<input type="text" name="fuga" value="2"></p>
			<p><button type="submit">Submit</button>
		</form>
	</body>
	</html>
	""".format(dice=dice)
	print(html)
else:
	# Params
	hoge = int(params.getvalue("hoge", default="none"))
	fuga = int(params.getvalue("fuga", default="none"))
	total = hoge + fuga
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
		<p>Total:{total}</p>
	</body>
	</html>
	""".format(dice=dice, hoge=hoge, fuga=fuga, total=total)
	print(html)