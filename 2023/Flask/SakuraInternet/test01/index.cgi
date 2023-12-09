#!/home/ozateck/.pyenv/versions/3.9.14/bin/python3
# Important!!

import cgitb
from wsgiref.handlers import CGIHandler
from app import app
from sys import path

cgitb.enable() # CGI
path.insert(0, "/home/ozateck/www/flask/test01/")

class ProxyFix(object):
	def __init__(self, app):
		self.app = app
	def __call__(self, environ, start_response):
		# ※要書き換え
		environ['SERVER_NAME'] = "ozateck.sakura.ne.jp"
		environ['SERVER_PORT'] = "80"
		environ['REQUEST_METHOD'] = "GET"
		environ['SCRIPT_NAME'] = ""
		environ['PATH_INFO'] = "/"
		environ['QUERY_STRING'] = ""
		environ['SERVER_PROTOCOL'] = "HTTP/1.1"
		return self.app(environ, start_response)

if __name__ == "__main__":
	app.wsgi_app = ProxyFix(app.wsgi_app)
	CGIHandler().run(app)