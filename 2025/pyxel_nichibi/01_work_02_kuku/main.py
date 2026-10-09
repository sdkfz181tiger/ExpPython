import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

# Work01
for i in range(5):
    x = i * 10
    y = 0
    pyxel.text(x, y, str(x), 7) # 白

# Work02
for i in range(5):
    x = 0
    y = i * 10
    pyxel.text(x, y, str(y), 8) # 赤

# Work03
for i in range(5):
    x = i * 10
    y = i * 10
    pyxel.text(x, y, str(i), 3) # 青

# 課題
# TODO: Lv1
#   九九表を作る事
# TODO: Lv2
#   3の倍数の時は"赤"、
#   それ以外は"白"
# TODO: Lv3
#   3の倍数の時は"赤"、
#   5の倍数の時は"青"、
#   3&5の倍数の時は"黄"、
#   それ以外は"白"

# 画面表示
pyxel.show()