# coding: utf-8

"""
SNSの画面をスクリーンショットする
	はてなブログ、はてなダイアリー、Qiita、Note
"""

import time
from my_modules.screen_manager import HatenaManager, QiitaManager, NoteManager

# HatenaBlog
# hatenablog_mng = HatenaManager("HatenaBlog")
for y in range(2022, 2023):
	for p in range(1, 2):
		url = "https://xxxxxxxxxx.hatenablog.com/archive/{}?page={}".format(str(y), str(p))
		hatenablog_mng.browse("./db/hatenablog.db", url, "entry")
		time.sleep(3)# Sleep

# HatenaDiary
# hatenadiary_mng = HatenaManager("HatenaDiary")
# for y in range(2021, 2022):
# 	for p in range(1, 2):
# 		url = "https://xxxxxxxxxx.hatenadiary.jp/archive/{}?page={}".format(str(y), str(p))
# 		hatenadiary_mng.browse("./db/hatenadiary.db", url, "entry")
# 		time.sleep(3)# Sleep

# Qiita
# qiita_mng = QiitaManager("Qiita")
# for p in range(1, 2):
# 	url = "https://qiita.com/xxxxxxxxxx?page={}".format(str(p))
# 	qiita_mng.browse("./db/qiita.db", url, "items")
# 	time.sleep(5)# Sleep

# Note
# note_mng = NoteManager("Note")
# for y in range(2021, 2022):
# 	url = "https://note.com/xxxxxxxxxx/archives/{}".format(str(y))
# 	note_mng.browse("./db/note.db", url, "xxxxxxxxxx/n")
# 	time.sleep(5)