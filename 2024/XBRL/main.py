# coding: utf-8

"""
1, Create Account
	URL: https://api.edinet-fsa.go.jp/api/auth/index.aspx?mode=1

2, EDINET(v2)
	https://api.edinet-fsa.go.jp/

3, Install
	$python3 -m pip install requests
	$python3 -m pip install urllib3

"""

#==========
# Main

import requests, urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

# API
#URL = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"
#URL = "https://api.edinet-fsa.go.jp/api/v1/documents.json"
URL = "https://api.edinet-fsa.go.jp/api/v2/documents.json?date=2022-04-01&type=2&Subscription-Key=ZZZ…ZZ"

def get_id(doc_date, doc_code, doc_type):

	# Params
	params = {"date": doc_date, type: 2}

	# Documents
	docs = requests.get(URL, params=params, verify=False)
	print(docs)

	results = docs.json()["results"]
	for result in results:
		if result["docTypeCode"] != doc_type: continue
		if result["edinetCode"] == doc_code: return id

	return -1

def main():
	print("main!!")

	# Test
	doc_date = "2023-06-30"
	doc_code = "E02367"# 任天堂
	doc_type = "120"# 有価証券報告書
	doc_id = get_id(doc_date, doc_code, doc_type)

	print("code: {}, id:{}".format(doc_code, doc_id))

if __name__ == "__main__":
	main()
