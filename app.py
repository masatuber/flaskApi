from flask import Flask, request, jsonify
import os
import subprocess
import platform
from flask_cors import CORS  # CORSのインポート

app = Flask(__name__)
CORS(app)  # CORSを適用

# デフォルトで開くディレクトリ
DEFAULT_DIRECTORY = r"C:\Users"

def open_directory(directory):
    """
    指定されたディレクトリをエクスプローラで開く関数
    """
    if not os.path.isdir(directory):
        raise ValueError('Invalid directory path')

    if platform.system() == "Windows":
        subprocess.run(["explorer", directory], check=True)
    else:
        subprocess.run(["open" if platform.system() == "Darwin" else "xdg-open", directory], check=True)


@app.route('/open-explorer', methods=['POST', 'GET'])
def open_explorer():
    """
    ディレクトリをエクスプローラで開くAPI
    POST: JSONボディでディレクトリを指定
    GET: クエリパラメータでディレクトリを指定
    """
    try:
        if request.method == 'POST':
            # POSTリクエストからディレクトリ取得
            data = request.json
            directory = data.get('directory', DEFAULT_DIRECTORY)
        elif request.method == 'GET':
            # GETリクエストからクエリパラメータを取得
            directory = request.args.get('directory', DEFAULT_DIRECTORY)

        # ディレクトリを開く
        open_directory(directory)

        return jsonify({'status': 'Explorer opened', 'directory': directory}), 200

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    # Flaskサーバーをデバッグモードで起動
    app.run(host='0.0.0.0', port=5000, debug=True)
