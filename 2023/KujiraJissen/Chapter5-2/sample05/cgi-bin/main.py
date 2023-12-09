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

import cgi, cgitb, os.path, html, datetime

FILE_LOG = "./log.txt"

# Debug
cgitb.enable()

# Print
def print_page(log):

	# Header
	print("Content-Type: text/html; charser=utf-8")
	print("")

	# HTML
	html = """
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="UTF-8">
		<title>Hello, World!!</title>
	</head>
	<body>
		<h1>Chat</h1>
		<p>
			<form>
				<p><input type="text" name="name" value="Alex"/></p>
				<p><input type="text" name="msg" value="Hello, World!!"/></p>
				<p><button type="submit">Submit</button></p>
				<input type="hidden" name="mode" value="write"/>
			</form>
		</p>
		<hr>
		{log}
	</body>
	</html>
	""".format(log=log)
	print(html)

# Read
def mode_read(params):
	log = ""
	with open(FILE_LOG, "r", encoding="utf-8") as file:
		log = file.read()
	print_page(log)

# Write
def mode_write(params):
	# GET
	name = params.getvalue("name", "noname")
	msg = params.getvalue("msg", "...")
	name = html.escape(name)
	msg = html.escape(msg)
	stamp = datetime.datetime.now().strftime("%Y/%m/%d_%H:%M:%S")
	# Write
	with open(FILE_LOG, "a", encoding="utf-8") as file:
		file.write("<p>{0}:{1}:{2}</p>".format(name, msg, stamp))
	# Redirect
	redirect_page("main.py")

# Redirect
def redirect_page(url):
	# Redirect
	print("Status: 301 Moved Permanently")
	print("Location: " + url)
	print("")
	# HTML
	html = """
	<!DOCTYPE html>
	<html>
	<head>
		<meta charset="UTF-8">
		<meta http-equiv="refresh" content="0;URL={url}">
		<title>Hello, World!!</title>
	</head>
	<body>
		<a href="{url}">Reflesh</a>
	</body>
	</html>
	""".format(url=url)
	print(html)

# Main
def main():
	# GET
	params = cgi.FieldStorage()
	# Mode
	mode = params.getvalue("mode", "read")
	if mode == "read": 
		mode_read(params)
	elif mode == "write": 
		mode_write(params)
	else:
		print_page("<p>Error...</p>")

if __name__=="__main__":
	main()