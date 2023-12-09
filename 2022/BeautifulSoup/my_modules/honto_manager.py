# coding: utf-8

import datetime, json, os, re, sys, time, urllib.error
import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# HontoManager
class HontoManager:

	def __init__(self, my_file):
		print("HontoManager: %s" % (my_file))
		# File
		self.my_file = my_file
		self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"}
		self.d_format = "%Y-%m-%d_%H-%M-%S"
		self.h_limit = 23 # 23時間経過

	def check(self):
		if(self.loadJSON()):# Load
			items = self.parseRoot("https://honto.jp", "/ranking.html")
			self.saveJSON(items)# Save
			return True
		return False

	def parseRoot(self, head, tail):
		print("parseRoot:%s" % (head + tail))
		# User Agent
		req = urllib.request.Request(head + tail, None, self.headers)
		# Open
		with urllib.request.urlopen(req) as res:
			bsoup = BeautifulSoup(res, "html.parser")

			# Dictionary
			title = bsoup.title.string
			date = datetime.datetime.now().strftime(self.d_format)
			items = dict(title=title, date=date, items=[])

			# Links
			links = bsoup.select("dl dd ul li a")
			for link in links:
				item = self.parseChild(head, link.attrs.get("href"))
				items["items"].append(item)
				# time.sleep(1)# Sleep
			return items

	def parseChild(self, head, tail):
		print("parseChild:%s" % (head + tail))
		try:
			# User Agent
			req = urllib.request.Request(head + tail, None, self.headers)
			# Open
			with urllib.request.urlopen(req) as res:
				bsoup = BeautifulSoup(res, "html.parser")

				# Dictionary
				title = bsoup.title.string
				items = dict(title=title, items=[])

				# Infos
				infos = bsoup.select("div[class='stInfo']")
				for info in infos:
					img = info.select_one("img")
					name = img.attrs.get("alt").strip()
					image = img.attrs.get("src").strip()
					item = dict(name=name, image=image)
					items["items"].append(item)
					self.saveImage(image)# Save(If you needed...)
				return items
		except urllib.error.HTTPError as e:
			print("HTTPError:%s" % (e.reason))
		except urllib.error.URLError as e:
			print("URLError:%s" % (e.reason))
		else:
			print("Good:%s" % (head + tail))

	def loadJSON(self):
		# JSON
		with open(self.my_file, mode="r") as f:
			items = json.load(f)
			d_file = datetime.datetime.strptime(items["date"], self.d_format)
			d_now = datetime.datetime.now()
			h_passed = (d_now.timestamp() - d_file.timestamp()) / 60 / 60
			print("File: %s" % (d_file.strftime(self.d_format)))
			print("Now: %s" % (d_now.strftime(self.d_format)))
			print("Passed: %s <-> Limit: %s" % (h_passed, self.h_limit))
		return self.h_limit < h_passed

	def saveJSON(self, items):
		# JSON
		enc = json.dumps(items, indent=2, ensure_ascii=False)
		with open(self.my_file, mode="w") as f:
			f.write(enc)
		# Archive json
		archive = os.path.split(self.my_file)[0] + "/" + items["date"] + "_index.json"
		with open(archive, mode="w") as f:
			f.write(enc)

	def saveImage(self, url):
		# Pattern
		ptn = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
		if(not re.match(ptn, url)):
			return False
		# Path
		path = os.path.split(self.my_file)[0] + urlparse(url).path
		if(os.path.isfile(path)): 
			return False
		else:
			os.makedirs(os.path.split(path)[0], exist_ok=True)
		# Image
		try:
			# User Agent
			req = urllib.request.Request(url, None, self.headers)
			# Open
			with urllib.request.urlopen(req) as res:
				data = res.read()
				with open(path, mode="wb") as f:
					f.write(data)
		except urllib.error.HTTPError as e:
			print("HTTPError:%s" % (e.reason))
		except urllib.error.URLError as e:
			print("URLError:%s" % (e.reason))
		else:
			print("Good:%s" % (path))

		return True
		
