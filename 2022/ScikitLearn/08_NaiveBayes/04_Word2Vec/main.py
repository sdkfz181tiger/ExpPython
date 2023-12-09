# coding: utf-8

"""
コーパス(コンピュータによる検索が可能な大量の言語データ)を作る

1, Wikipedia日本語全文データ(3Gもあります):

	URL: https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2

	curl URL -o jawiki-latest-pages-articles.xml.bz2
	bzip2 -d jawiki-latest-pages-articles.xml.bz2

2, データをテキスト化

	ruby2.3.0をインストール
		brew install rbenv
		rbenv init
		eval "$(rbenv init -)"
		ターミナル再起動
		rbenv
		rbenv install -l
		rbenv install 2.3.0

	wp2txtをインストール
		gem install wp2txt

	wp2txtでxmlをテキストファイルに
		wp2txt --input ./jawiki-latest-pages-articles.xml

3, 形態素解析して分かち書き化

	分割ファイルを一つにまとめる
		cat jawiki-latest-pages-articles-* > wiki.wp2txt

	まとめたテキストファイルをMeCabで分かち書きする
		mecab -b 100000 -Owakati wiki.wp2txt -o wiki_wakati.txt

"""

import MeCab
import numpy as np
from gensim.models import word2vec

# Word2Vec
print("Hello Word2Vec!!")

# コーパスの読み込み
# sentences = word2vec.Text8Corpus("./wiki_wakati.txt")
# モデルの作成(数時間かかります)
# sg: Word2Vecで扱うアルゴリズム 0:CBOW(速度重視), 1:Skip-gram(精度重視)
# vector_size: ベクトルの次元を設定
# window: 学習する単語の前後数
# clf = word2vec.Word2Vec(sentences, sg=0, vector_size=100, window=5, min_count=5)
# clf.save("./wiki_corpus.model")

# モデル
clf = word2vec.Word2Vec.load("./model/wiki.model")

#==========
# 1, 関連語を計算
#results = clf.wv.most_similar(positive=["業務"])
#for result in results: print(result)

#==========
# 2, 関連語の足し算と引き算
#results = clf.wv.most_similar(positive=["王", "女"], negative=["男"])
#for result in results: print(result)

#==========
# 3, Mecabオブジェクト(辞書を指定)
tagger = MeCab.Tagger("-d /var/lib/mecab/dic/mecab-ipadic-neologd")
tagger.parse("")

# keywordと、渡されたtextに含まれる各単語との類似語をチェックする
def check_emergency(keyword, txt):
	print(txt)
	# 形態素解析
	node = tagger.parseToNode(txt)
	while node is not None:
		# ストップワードを除く
		field = node.feature.split(",")[0]
		if field == "名詞" or field == "動詞" or field == "形容詞":
			# 類似度を表示する
			print(clf.wv.similarity(node.surface, keyword))
		node = node.next

# "至急"との類似語をチェックする
check_emergency("至急", "PCが起動しなくなりました。急いでいます。")
check_emergency("至急", "使い方がよくわかりません。")
