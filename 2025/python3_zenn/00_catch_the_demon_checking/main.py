import tkinter

# キャンバスの幅と高さ
W, H = 480, 320

# フレームレート
F_RATE = 30 # 1秒間に実行するフレーム回数
F_INTERVAL = int(1000 / F_RATE) # 1フレームの間隔

# 背景画像とイメージ(グローバル変数)
bg_photo, bg_image = None, None

def init():
    """ 初期化関数 """
    global bg_photo, bg_image # グローバル変数を指定

    # 背景
    bg_photo = tkinter.PhotoImage(file="images/bg_jigoku.png")
    bg_image = cvs.create_image(W/2, H/2, image=bg_photo)

def update():
    """ 更新関数 """
    # 画面更新
    root.after(F_INTERVAL, update)

# Tkinter
root = tkinter.Tk()
root.title("Hello, Tkinter!!")
root.resizable(False, False)

# キャンバス
cvs = tkinter.Canvas(width=W, height=H, bg="black")
cvs.pack()
init()
update()
root.mainloop()
