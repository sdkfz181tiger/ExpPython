# coding: utf-8

"""
Hello World
"""

#==========
# Main

# Dictionary

member = {"jojo": "承太郎", "joseph": "ジョセフ", "abdul": "アヴドゥル"}
member["kakyoin"] = "花京院"
print(member)
# {'jojo': '承太郎', 'joseph': 'ジョセフ', 'abdul': 'アヴドゥル', 'kakyoin': '花京院'}

print(list(member.keys()))# キーのみ(ソート未)
# ['jojo', 'joseph', 'abdul', 'kakyoin']

print(sorted(member.keys()))# キーのみ(ソート済)
# ['abdul', 'jojo', 'joseph', 'kakyoin']

# キーの存在を確認
print("kakyoin" in member)# True
print("polnareff" in member)# False
print("iggy" in member)# False

# タプルからディクショナリを作る
