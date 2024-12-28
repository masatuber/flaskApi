import os
import platform
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

# Flaskアプリケーションの初期化
app = Flask(__name__)

# CORSを有効化（すべてのオリジンを許可）
CORS(app)

@app.route('/open-explorer', methods=['POST'])
def open_explorer():
    try:
        # リクエストからディレクトリパスを取得
        directory = request.json.get('directory', 'C:\\Users')

        # ディレクトリが存在するかチェック
        if not os.path.isdir(directory):
            return jsonify({'error': 'Invalid directory path'}), 400

        # OSに応じてエクスプローラーを開く
        if platform.system() == "Windows":
            subprocess.run(["explorer", directory], check=True)
        elif platform.system() == "Darwin":  # macOSの場合
            subprocess.run(["open", directory], check=True)
        else:  # Linuxの場合
            subprocess.run(["xdg-open", directory], check=True)

        return jsonify({'status': f'Explorer opened at {directory}'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':

    # Flaskサーバーをデバッグモードで起動
    app.run(host='0.0.0.0', port=5000, debug=True)
