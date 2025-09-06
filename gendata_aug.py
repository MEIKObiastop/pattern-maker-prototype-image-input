# データを増幅して精度を向上させよう
# 実行方法　python gendata_aug.py

from PIL import Image, ImageEnhance
import glob
import numpy as np

classes = ["jacket","onepiece","pants","skirt","tops"]
image_size = 50
# テストデータ数(データが少ないため、テスト用は少なくする)
num_testdata = 1

X_train = []
X_test = []
Y_train = []
Y_test = []

# 画像を増幅して学習データを増やす
for index, classlabel in enumerate(classes):
# ***教材コード***
            # 画像を開いてRGB変換＆リサイズ
            # 形状チェック
                # 学習データ
                # 元画像も追加
                # 増幅処理（回転と反転）
                    # 左右反転

                    # 彩度を下げる（0.0 = モノクロ, 1.0 = 元の色）
                    enhancer = ImageEnhance.Color(image)
                    img_low_saturation = enhancer.enhance(0.5)  # 彩度半分
                    data_low = np.asarray(img_low_saturation, dtype=np.float32) / 255.0
                    X_train.append(data_low)
                    Y_train.append(index)
                    
                    # 明るさ
                    enhancer = ImageEnhance.Brightness(image)
                    img_bright = enhancer.enhance(1.5)  # 1.5倍明るく
                    X_train.append(np.asarray(img_bright, dtype=np.float32)/255.0)
                    Y_train.append(index)

                    # コントラスト
                    enhancer = ImageEnhance.Contrast(image)
                    img_contrast = enhancer.enhance(1.3)  # コントラスト強調
                    X_train.append(np.asarray(img_contrast, dtype=np.float32)/255.0)
                    Y_train.append(index)


        except Exception as e:
            print(f"Error loading {file}: {e}")

# NumPy配列に変換
# ***教材コード***

# 保存
np.save("X_train.npy", X_train)
np.save("X_test.npy", X_test)
np.save("y_train.npy", y_train)
np.save("y_test.npy", y_test)

print("Data saved!")
print("X_train:", X_train.shape, "X_test:", X_test.shape)