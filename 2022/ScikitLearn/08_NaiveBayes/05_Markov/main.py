# coding: utf-8

"""
マルコフ連鎖_文章自動生成(簡易)
"""

import MeCab, random

# Markov
print("Hello Markov!!")

def load_txt():
	file = open("./data.txt", "r", encoding="UTF-8")
	data = file.read()
	file.close()
	return data

def set_dic(dic, w1, w2, w3):
	if w1 not in dic: dic[w1] = {}
	if w2 not in dic[w1]: dic[w1][w2] = {}
	if w3 not in dic[w1][w2]: dic[w1][w2][w3] = 0
	dic[w1][w2][w3] += 1

def create_dic(dic, nouns, txt):
	# MeCab
	tagger = MeCab.Tagger("-d /var/lib/mecab/dic/mecab-ipadic-neologd")
	tagger.parse("")
	# Parse
	node = tagger.parseToNode(txt)
	lines = []
	while node is not None:
		if node.surface != "「" and node.surface != "」" :
			lines.append(node)
		node = node.next

	for i in range(len(lines)-4):
		# 辞書を作る
		w1 = lines[i].surface
		w2 = lines[i+1].surface
		w3 = lines[i+3].surface
		set_dic(dic, w1, w2, w3)
		# 名詞リストを作る
		hinshi = lines[i].feature.split(",")[0]
		if(hinshi == "名詞"): nouns.append(lines[i].surface)

def create_msg(dic, nouns):
	# 名詞リストからランダム
	w1 = nouns[random.randrange(len(nouns))]
	msg = w1

	# TODO: カウント数に応じて優先的に選択する
	while True:
		keys1 = dic[w1]
		w2 = random.choice(list(keys1))
		msg = msg + w2
		if(w2 == "。"): break
		keys2 = dic[w1][w2]
		w3 = random.choice(list(keys2))
		msg = msg + w3
		if(w3 == "。"): break
		w1 = w3
	return msg

# Test
dic = {}# 辞書
nouns = []# 名詞リスト
txt = load_txt()
create_dic(dic, nouns, txt)
msg = create_msg(dic, nouns)
print(msg)


