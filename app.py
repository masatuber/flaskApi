from flask import Flask, request, jsonify
import os
import subprocess
import platform
from flask_cors import CORS # CORSのインポート

# Flaskアプリケーションの初期化
app = Flask(__name__)

# CORSを有効化（すべてのオリジンを許可）
CORS(app)

@app.route('/open-explorer', methods=['POST'])
def open_explorer():
    # リクエストからディレクトリパスを取得
    directory = request.json.get('directory', 'C:\\Users')
    
    # 実行処理（ここではダミーレスポンス）
    return jsonify({'status': f'Explorer opened at {directory}'})

if __name__ == '__main__':

    # Flaskサーバーをデバッグモードで起動
    app.run(host='0.0.0.0', port=5000, debug=True)
