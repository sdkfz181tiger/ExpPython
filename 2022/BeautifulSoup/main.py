# coding: utf-8

"""
sudo pip install --upgrade pip
	pip install requests
	pip install bs4
"""

from my_modules.honto_manager import HontoManager

# HontoManager
my_file = "./contents/index.json"
h_manager = HontoManager(my_file)
print("Checking...")
if(h_manager.check()):# Check
	print("Updated...")
else:
	print("Do nothing...")