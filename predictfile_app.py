from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
from keras.models import load_model
import numpy as np
from PIL import Image
import os

classes = ["jacket","onepiece","pants","skirt","tops"]
image_size = 50

UPLOAD_FOLDER = './static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# staticを静的ファイルとして扱えるようにする
app.static_folder = 'static'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# 学習済みモデルを先にロード（毎回ロードしない）
model = load_model('./fashion_cnn_aug.h5')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    uploaded_image_url = None
    result_text = None
    
# ***教材コード***

            # static から参照するパス
            uploaded_image_url = url_for('static', filename=filename)

            # 画像解析
# ***教材コード***

    return render_template('index.html', uploaded_image_url=uploaded_image_url, result_text=result_text, upload_label=upload_label)


@app.route('/pattern', methods=['POST'])
def make_pattern():
    # パターン作成処理はまだないので、トップに戻す
    return redirect(url_for('upload_file'))

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
