# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter2-5: 
	BMI判定プログラムを作ってみよう
"""

print("Hello, Python!!")

# ユーザーからの入力
n_weight = int(input("体重(kg)を入力してください"))
n_height = int(input("身長(cm)を入力してください"))

# 計算をする
n_bmi = n_weight / ((n_height/100)**2)

# 判定をする
msg = ""
if(n_bmi < 18.5):
	msg = "痩せ型"
elif(18.5 <= n_bmi) and (n_bmi < 25):
	msg = "標準型"
elif(25 <= n_bmi) and (n_bmi < 30):
	msg = "肥満(軽)"
else:
	msg = "肥満(重)"

print("BMI値:{0}".format(n_bmi))
print("判定:{0}".format(msg))
