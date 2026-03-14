# coding: utf-8

"""
[ アルトレ第二版 ]
4.8: ハッシュ法でデータを登録する
※プログラムの場合、配列の要素は0から始まる
"""

# 15行2列の2次元配列
hash_tbl = [[0 for _ in range(2)] for _ in range(15)]

idx = 5

def hash(data):
    global idx

    for i in range(len(data)):
        # ハッシュ位置を計算 0 ~ 4
        h = data[i] % 5
        if hash_tbl[h][0] == 0:
            # 空いていれば、データを格納する
            hash_tbl[h][0] = data[i]
        else:
            # 空いていない場合、チェーンを辿る...
            while h != 0:
                k = h
                h = hash_tbl[h][1]

            # チェーンの最後に格納し、チェーンを繋ぐ...
            hash_tbl[idx][0] = data[i] # データを格納
            hash_tbl[k][1] = idx # 次のチェーン位置
            idx = idx + 1

def main():
    """ メイン処理 """

    print("Before:", hash_tbl)
    hash([4, 12, 17, 18, 22])
    print("After:", hash_tbl)

if __name__ == "__main__":
    main()