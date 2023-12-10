# coding: utf-8

"""
スッキリわかる機械学習入門より
1, Install
	$ python3 -m pip install pandas
	$ python3 -m pip install scikit-learn
"""

import pandas as pd
import pickle
from sklearn import tree

FILE_CSV = "./data.csv"
FILE_PKL = "./data.pkl"
COLUMNS_X = ["cm", "kg", "era"]
COLUMNS_T = "group"

#==========
# Data

def main():
	print("main!!")
	
	# Create
	create_model()

	# Predict
	taro = [165, 60, 30]
	jiro = [170, 70, 20]
	sabu = [175, 75, 10]
	bros = [taro, jiro, sabu]
	result = predict_model(bros)
	print("Result:", result)

def create_model():
	print("create_model!!")
	# Read
	df = pd.read_csv(FILE_CSV)
	# Split
	x = df[COLUMNS_X]
	t = df[COLUMNS_T]
	# Model
	model = tree.DecisionTreeClassifier(random_state=0)
	# Learn
	model.fit(x, t)
	# Score
	print("Score:", model.score(x, t))
	# Save
	pickle.dump(model, open(FILE_PKL, "wb"))

def predict_model(arr):
	print("predict_model!!")
	model = pickle.load(open(FILE_PKL, "rb"))
	# Predict
	df = pd.DataFrame(arr, columns=COLUMNS_X)
	return model.predict(df)

if __name__ == "__main__":
	main()