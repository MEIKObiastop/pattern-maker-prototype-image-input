# -*- coding: utf-8 -*-
# python download.py "学習したいキーワード"　仮想環境で実行

import os, sys, time
import requests

API_KEY = "52124319-c07c91cfcd7287d76923102bc"
wait_time = 1

# コマンドライン引数で検索キーワードを取得
# ***教材コード***

keyword = sys.argv[1]

# 画像保存先フォルダ
savedir = os.path.join(keyword)
os.makedirs(savedir, exist_ok=True)

# Pixabay API へリクエスト
url = "https://pixabay.com/api/"
params = {
    "key": API_KEY,
    "q": keyword,
    "image_type": "photo",
    "per_page": 100,
    "safesearch": "true"
}

response = requests.get(url, params=params)
data = response.json()
hits = data.get("hits", [])

# 画像をダウンロード
# ヘッダーはループ外で定義

# ***教材コード***

print("ダウンロード完了！")