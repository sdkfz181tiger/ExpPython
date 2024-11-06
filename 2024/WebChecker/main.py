# coding: utf-8

"""
指定サイトをスクリーンショットする
"""

from my_modules.web_checker import WebChecker

# WebChecker
url = "https://sdkfz181tiger.github.io/ExpPiyoApps/"
wc = WebChecker("my_prefix")
wc.browse(url)
