# coding: utf-8

"""
Hello World
"""

#==========
# Main

# Listのメソッド各種

member = ["承太郎", "ジョセフ"]
member.append("アヴドゥル")# 追加

print(member)
# ['承太郎', 'ジョセフ', 'アヴドゥル']

member.remove("ジョセフ")# 削除
print(member)
# ['承太郎', 'アヴドゥル']

member.insert(1, "ジョセフ")# 指定位置に挿入
print(member)
# ['承太郎', 'ジョセフ', 'アヴドゥル']

others = ["花京院", "ポルナレフ", "イギー"]
member.extend(others)# 他シーケンスと連結
print(member)
# ['承太郎', 'ジョセフ', 'アヴドゥル', '花京院', 'ポルナレフ', 'イギー']

print("pop:", member.pop(0)) # 先頭から取り出す
print("pop:", member.pop(0)) # 先頭から取り出す
print("pop:", member.pop(1)) # 指定位置から取り出す
print("pop:", member.pop()) # 最後尾から取り出す
print(member)
# ['アヴドゥル', 'ポルナレフ']

member.insert(0, "イギー")
member.insert(0, "イギー")
member.append("イギー")
member.append("イギー")
print(member)
# ['イギー', 'イギー', 'アヴドゥル', 'ポルナレフ', 'イギー', 'イギー']

print(member.index("アヴドゥル"))# 位置を返す 2
print(member.index("ポルナレフ"))# 位置を返す 3
print(member.count("イギー"))# 数を数える 4

member.clear()# 全て削除
print(member)
# []

member.extend(["承太郎", "ジョセフ", "アヴドゥル", "花京院", "ポルナレフ", "イギー"])
print(member)
# ['承太郎', 'ジョセフ', 'アヴドゥル', '花京院', 'ポルナレフ', 'イギー']

member.reverse()# 逆順に並び替え
print(member)
# ['イギー', 'ポルナレフ', '花京院', 'アヴドゥル', 'ジョセフ', '承太郎']
