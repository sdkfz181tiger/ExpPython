#!/home/ozateck/.pyenv/versions/3.9.14/bin/python3
# Important!!

"""
	1, Flaskをインストール
		$ python3 -m pip install flask

	2, Pythonまでのパスを調べてcgi先頭に記述
		/home/xxx/.pyenv/versions/3.9.14/bin/python3

	3, index.cgiに実行権を付与
		$ ls -al
		$ chmod 755 index.cgi
"""

from flask import Flask

# Instance
app = Flask(__name__)

# Routing
@app.route("/")
def hello_world():
	return "<h1>Hello, Sakura Internet and Flask!!</h1>"

# Appを起動
if __name__ == "__main__":
	app.run()