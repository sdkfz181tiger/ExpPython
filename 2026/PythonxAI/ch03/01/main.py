# coding: utf-8

"""
1, Install
    $ python3 -m pip install torch
"""

import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST

DIR_DATA = "../data"
BATCH_SIZE = 8

def main():
    """ Main """
    print("main")

    # 訓練用データを用意する
    # 第一引数: ダウンロード先ディレクトリ
    # train: 訓練用データ
    # download: データをダウンロードする
    # transform: テンソルに変換
    d_mnist = MNIST(DIR_DATA, 
        train=True, download=True,
        transform=transforms.ToTensor())

    d_loader = DataLoader(d_mnist, 
        batch_size=BATCH_SIZE,
        shuffle=False)

    # データを確認
    d_iterator = iter(d_loader)
    images, labels = next(d_iterator)

    index = 0

    # 画像
    d_image = images[index].numpy()
    d_reshaped = d_image.reshape(28, 28)
    plt.imshow(d_reshaped, 
        cmap="inferno", 
        interpolation="bicubic")
    plt.show()

    # ラベル
    print("label:", labels[index])
    # label: tensor(5)


if __name__ == "__main__":
    main()