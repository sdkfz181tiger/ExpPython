# coding: utf-8

"""
1, Install
    $ python3 -m pip install ultralytics
"""

from ultralytics import YOLO, solutions

def main():
    """ Main """
    print("main")

    #train()    # 学習をテスト
    #validate() # 検証をテスト <- 試す時にコメントアウト
    predict()  # 推論をテスト <- 試す時にコメントアウト


def train():
    """ 学習 """

    # Model(ベースになるモデル)
    model = YOLO("yolo26n.pt")
    #model = YOLO("./runs/detect/train/weights/last.pt") # 最終エポック終了時点からの続き

    # Train
    # 学習(任意のデータセットを利用)
    # 最初は5エポックで様子を見る...
    results = model.train(
        data="./my_dataset/dataset.yaml",
        device="cpu", # mps: Apple Silicon
        epochs=30, 
        imgsz=640)


def validate():
    """ 検証 """

    # Model
    model = YOLO("./runs/detect/train/weights/best.pt") # 学習中に最も良い評価結果を出したモデル
    #model = YOLO("./runs/detect/train/weights/last.pt") # 最終エポック終了時点のモデル
    
    # Validate
    metrics = model.val()

    # 0.5から0.95までの複数のIoU閾値における平均適合率
    print(metrics.box.map)   # mAP50-95
    print(metrics.box.map50) # mAP50
    print(metrics.box.map75) # mAP75
    print(metrics.box.maps)  # 各クラス別の適合率


def predict():
    """ 推論 """

    # Model
    model = YOLO("./runs/detect/train/weights/best.pt")

    # Predict
    # ./runs/detect/predict/bus.jpg
    results = model.predict(
        source=[
            "cat01.jpg", "cat02.jpg", "cat03.jpg", 
            "cat04.jpg", "cat04.jpg", "cat05.jpg",
            "cat06.jpg"],
            # "buri1.jpg", "buri2.jpg", "buri3.jpg", 
            # "buri4.jpg", "buri5.jpg", "buri6.jpg"],
        save=True)
    print(results)


if __name__ == "__main__":
    main()