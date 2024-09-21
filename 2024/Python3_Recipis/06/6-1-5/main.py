# coding: utf-8

"""
文字列の検索、操作
"""

#==========
# Main

# 文字列を検索し、位置を返す
print("abcdefghijk".find("efg"))
# 4

# 文字列を検索し、位置を返す(存在しない場合)
print("abcdefghijk".find("xyz"))
# -1

# 文字列を分割し配列に格納
msg1 = "sun mon tue wed thu fri sat"
msgs = msg1.split()
msg2 = "_".join(msgs)

print(msg1)
# sun mon tue wed thu fri sat
print(msgs)
# ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
print(msg2)
# sun_mon_tue_wed_thu_fri_sat

# 接頭辞が一致する文字列か調べる
prefix = ("hop", "step", "jump")
print("step.png".startswith(prefix))# True
print("stop.txt".startswith(prefix))# False

# 接尾辞が一致する文字列か調べる
suffix = ("png", "jpg", "gif")
print("step.png".endswith(suffix))# True
print("stop.txt".endswith(suffix))# False
