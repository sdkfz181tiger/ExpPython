# coding: utf-8

"""
1, Install
    $ python3 -m pip install torch
"""

import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.optim as opt
import torchvision.transforms as transforms
from torch.autograd import Variable
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST

DIR_DATA = "../data"
BATCH_SIZE = 8

def main():
    """ Main """
    print("main")

    # 訓練用/検証用データを用意する
    # 第一引数: ダウンロード先ディレクトリ
    # train: 訓練用データ
    # download: データをダウンロードする
    # transform: テンソルに変換

    # 訓練用データ
    d_train = DataLoader(
        MNIST(DIR_DATA, train=True, download=True,
            transform=transforms.ToTensor()),
        batch_size=BATCH_SIZE, shuffle=True)
    print(d_train.dataset)
    """
    Dataset MNIST
        Number of datapoints: 60000
        Root location: ../data
        Split: Train
        StandardTransform
    Transform: ToTensor()
    """

    # 検証用データ
    d_test = DataLoader(
        MNIST(DIR_DATA, train=False, download=True,
            transform=transforms.ToTensor()),
        batch_size=BATCH_SIZE, shuffle=True)
    print(d_test.dataset) 
    """
    Dataset MNIST
        Number of datapoints: 10000
        Root location: ../data
        Split: Test
        StandardTransform
    Transform: ToTensor()
    """

    # 多層パーセプトロン(Multi Layer Perceptron)

    # 2つの中間層を持つMLPクラス
    class MLP(nn.Module):
        def __init__(self):
            super().__init__()
            # 入力と出力の数を合わせている
            self.layer1 = nn.Linear(28*28, 100)
            self.layer2 = nn.Linear(100, 50)
            self.layer3 = nn.Linear(50, 10)

        def forward(self, data):
            data = data.view(-1, 28*28)
            data = self.layer1(data)
            data = self.layer2(data)
            data = self.layer3(data)
            return data

    # モデルの生成
    model = MLP()

    # 誤差項(クロスエントロピー)と最適化器(Stochastic Gradient Descent)
    loss_result = nn.CrossEntropyLoss()
    optimizer = opt.SGD(model.parameters(), lr=0.01)

    # 学習なしでテスト
    #test(model, d_test)
    # total:10000, correct:1162, rate:0.12 <- 学習前
    
    # 学習をする
    MAX_EPOCH = 4
    for epoch in range(MAX_EPOCH):
        loss_total = 0.0
        for i, data in enumerate(d_train):
            d, labels = data
            d, labels = Variable(d), Variable(labels)

            # 勾配情報をリセット
            optimizer.zero_grad()
            loss = loss_result(model(d), labels)
            loss.backward()

            # 勾配を更新
            optimizer.step()

            # 誤差を積み上げる
            loss_total += loss.data

            if i % 2000 == 1999:
                print(f"学習進捗:{epoch+1}, {i+1}", end=" ")
                print(f"学習誤差:{loss}: {loss_total/2000:.3f}")
                loss_total = 0.0

    print("学習終了")

    # 学習後にテスト
    test(model, d_test)
    # total:10000, correct:9233, rate:0.92 <- 学習後

    # 個別データで検証
    iter_test = iter(d_test)
    t_data, labels = next(iter_test)
    results = model(Variable(t_data))
    _, predicted = torch.max(results.data, 1)

    # 最初のデータを検証
    index = 0
    plt.imshow(
        t_data[index].numpy().reshape(28, 28),
        cmap="inferno", interpolation="bicubic")
    plt.show()
    print("label:", predicted[index])
    # label: tensor(9)


def test(model, d_test):
    """ テスト """
    cnt_total = 0
    cnt_correct = 0
    for data in d_test:
        d, labels = data
        results = model(Variable(d))
        _, predicted = torch.max(results.data, 1)
        cnt_total += labels.size(0)
        cnt_correct += (predicted==labels).sum()

    rate = "{:.2f}".format(cnt_correct/cnt_total)
    print(f"total:{cnt_total}, correct:{cnt_correct}, rate:{rate}")


if __name__ == "__main__":
    main()