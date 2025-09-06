# モデルをトレーニングする
# 実行方法　python fashion_cnn_aug.py


from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.utils import to_categorical
import keras
import numpy as np

classes = ["jacket","onepiece","pants","skirt","tops"]
num_classes = len(classes)
image_size = 50

def main(X_train, X_test, y_train, y_test):
    # 255で割って0~1の値に正規化する (今回はgen_data.pyで正規化済み)
    X_train = np.array(X_train, dtype=np.float32)
    X_test = np.array(X_test, dtype=np.float32)
    
    # to_categorical関数でone-hotベクトル形式に変換する
    y_train = to_categorical(y_train, num_classes)
    y_test = to_categorical(y_test, num_classes)

	# トレーニングの実行
    model = model_train(X_train, y_train)
    # モデルの精度評価（未使用データの推定精度を計算する）
    model_eval(model, X_test, y_test)
    

def model_train(X, y):
# ***教材コード***

    # モデルの保存
    model.save('./fashion_cnn_aug.h5')

    return model


def model_eval(model, X, y):
# ***教材コード***
    

def model_predict(model, X, y):
# ***教材コード***

if __name__ == "__main__":
    X_train = np.load("X_train.npy")
    X_test = np.load("X_test.npy")
    y_train = np.load("y_train.npy")
    y_test = np.load("y_test.npy")
    main(X_train, X_test, y_train, y_test)