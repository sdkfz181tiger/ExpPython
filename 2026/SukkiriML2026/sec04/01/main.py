# coding: utf-8

"""
1, Install
	$ python3 -m pip install pandas
"""

import pandas as pd

#==========
# Main

data = {
	"Alex": [100, 160],
	"Becky": [80, 180]
}

def main():
	print("main!!")
	
	# DataFrame
	df = pd.DataFrame(data)
	print(df)

	# Type
	print("Type:", type(df))
	print("shape:", df.shape)

	# 行名の変更
	df.index = ["Apr", "May"]
	print(df)

	# 列名の変更
	df.columns = ["Cathy", "Mike"]
	print(df)

	# 行名, 列名
	print(df.index)
	print(df.columns)

if __name__ == "__main__":
	main()