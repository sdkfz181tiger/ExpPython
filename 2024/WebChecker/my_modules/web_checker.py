# coding: utf-8

import datetime, os, sys, time
import chromedriver_binary # For Mac and Linux
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By


# MainChecker
class MainChecker:

	def __init__(self, prefix):
		print(f"MainChecker: {prefix}")
		# Make directory
		self.dir_path = os.path.join("images", prefix)
		os.makedirs(self.dir_path, exist_ok=True)

	def browse(self, url):
		print(f"browse: {url}")

		# Launch browser
		driver = webdriver.Chrome(options=self.get_options())
		driver.set_window_size(1400, 2000)
		driver.get(url)# Get
		time.sleep(5)# Sleep

	def get_options(self):
		# Options
		options = webdriver.ChromeOptions()
		options.add_argument("start-maximized")
		options.add_argument("enable-automation")
		options.add_argument("--headless")
		options.add_argument("--no-sandbox")
		options.add_argument("--disable-infobars")
		options.add_argument('--disable-extensions')
		options.add_argument("--disable-dev-shm-usage")
		options.add_argument("--disable-browser-side-navigation")
		options.add_argument("--disable-gpu")
		options.add_argument('--ignore-certificate-errors')
		options.add_argument('--ignore-ssl-errors')
		prefs = {"profile.default_content_setting_values.notifications" : 2}
		options.add_experimental_option("prefs", prefs)
		return options


# WebChecker
class WebChecker(MainChecker):

	def __init__(self, prefix):
		super().__init__(prefix)
		print("WebChecker")