# coding: utf-8

"""
実践力を身につけるPythonの教科書より
Chapter2-6: 
	繰り返し処理2:FizzBuzz問題をやってみよう
"""

print("Hello, Python!!")

for i in range(30):

	if(i%3 == 0 and i%5 ==0):
		print("{0}:FizzBuzz".format(i))
		continue
	if(i%3 == 0):
		print("{0}:Fizz".format(i))
		continue
	if(i%5 == 0):
		print("{0}:Buzz".format(i))
		continue