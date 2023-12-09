# coding: utf-8

"""
1, 単語頻出データを作る

スパムテキスト(クジラ飛行机先生のGitHubから)
	https://github.com/kujirahand/spam-database-ja

非スパムテキスト(LiveDoorニュースから)
	https://www.rondhuit.com/download.html#ldcc
	ldcc-20140209.tar.gz
"""

import glob, os, pickle, MeCab
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Bayesian Filter
print("Hello Bayesian Filter!!")

FILE_PICKLE = "./words.pickle"# 単語頻出データ
FILE_MODEL = "./words.model"# 学習済データ

# MeCab
tagger = MeCab.Tagger("-d /var/lib/mecab/dic/mecab-ipadic-neologd")
tagger.parse("")

# 1, 単語頻出データを作る
def create_pickle():
	print("Create pickle...")

	# 保存ファイル
	word_ids = {"__id": 0}# 単語辞書
	word_data = []# 単語データ

	# フォルダの読み込み
	def read_dir(dir, label):
		files = glob.glob(dir + "/*.txt")
		for file in files: read_file(file, label)

	# ファイルの読み込み
	def read_file(file, label):
		with open(file, "rt", encoding="utf-8") as f:
			txt = f.read()
			word_data.append({"label": label, "words": text_to_id(txt)})

	# テキストを単語IDのリストに変換
	def text_to_id(txt):
		# 形態素解析
		node = tagger.parseToNode(txt)
		result = []
		while node is not None:
			feature = node.feature.split(",")
			hinshi = feature[0]# 品詞
			origin = feature[6]# 原形
			if hinshi in ["名詞", "動詞", "形容詞"]:
				result.append(word_to_id(origin))
			node = node.next
		return result

	def word_to_id(word):
		if not (word in word_ids):# 新規登録(通し番号を振る)
			id = word_ids["__id"]
			word_ids["__id"] += 1
			word_ids[word] = id
		else:
			id = word_ids[word]
		return id

	def create_freq_words():
		y = []
		x = []
		for d in word_data:
			y.append(d["label"])
			x.append(create_freq_data(d["words"]))
		return y, x

	def create_freq_data(words):
		# 単語の出現回数
		cnt = 0
		dat = np.zeros(word_ids["__id"], "float")
		for w in words:
			cnt += 1
			dat[w] += 1
		# 出現頻度に変換
		dat = dat / cnt
		return dat

	# フォルダの読み込み
	read_dir("./filters/ok", 0)# OK(通常の文章)
	read_dir("./filters/ng", 1)# NG(スパムメール)
	y, x = create_freq_words()
	# ファイルに保存(0:x, 1:y, 2:word_ids)
	pickle.dump([y, x, word_ids], open(FILE_PICKLE, "wb"))

# 2, 機械学習
def create_model():
	print("Create model...")

	# 単語頻出データ
	data = pickle.load(open(FILE_PICKLE, "rb"))
	y = data[0]# ラベル
	x = data[1]# 出現頻度

	# テストを100回繰り返す
	total = 100
	rate = 0
	for i in range(total):
		# データを学習用とテスト用に分割
		x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
		# 学習
		clf = GaussianNB()
		clf.fit(x_train, y_train)
		# 評価
		y_pred = clf.predict(x_test)
		acc = accuracy_score(y_test, y_pred)
		# 結果が良ければモデルを保存
		if 0.94 < acc: pickle.dump(clf, open(FILE_MODEL, "wb"))
		print("accuraty:", acc)
		rate += acc

	print("average:", rate / total)

# 3, スパム判定
def check_spam(txt):
	print("Check spam:", txt)

	# 単語頻出データ
	data = pickle.load(open(FILE_PICKLE, "rb"))
	word_ids = data[2]# word_ids

	# 学習済モデル
	clf = pickle.load(open(FILE_MODEL, "rb"))
	# 単語IDのリストに変換し単語の出現頻度を調べる
	arr = np.zeros(word_ids["__id"])
	total = 0

	# 形態素解析
	node = tagger.parseToNode(txt)
	while node is not None:
		feature = node.feature.split(",")
		origin = feature[6]# 原形
		if origin in word_ids:
			id = word_ids[origin]
			arr[id] += 1
			total += 1
		node = node.next
	# 出現頻度に変換
	arr = arr / total
	# 予測
	return clf.predict([arr])[0]

#==========
# 1, 単語頻出データを作る
create_pickle()
print("データ作成完了")

#==========
# 2, 機械学習
create_model()
print("データ学習完了")

#==========
# 3, スパム判定
txt1 = "お昼のニュースです。今日の日経平均株価は、大幅に下がり3万円を大幅に下回りました。"
txt2 = "簡単に億万長者になる方法を教えます。今すぐにこのアカウントにダイレクトメールを送ってください!!"
result = check_spam(txt1)# 0:安全, 1:スパム
if result == 0:
	print("このメールは安全です")
else:
	print("このメールはスパムです")
