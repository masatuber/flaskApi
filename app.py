import os
import platform
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/open-explorer', methods=['POST'])
def open_explorer():
    try:
        # JSONデータを取得
        data = request.get_json()
        if not data or 'directory' not in data:
            return jsonify({'error': 'Missing "directory" in request JSON'}), 400

        # ディレクトリパスを取得
        directory = data.get('directory', 'C:\\Users')

        # ディレクトリの存在確認
        if not os.path.isdir(directory):
            return jsonify({'error': f'Invalid directory path: {directory}'}), 400

        # OSに応じてエクスプローラーを開く
        if platform.system() == "Windows":
            subprocess.run(["explorer", directory], check=True)
        elif platform.system() == "Darwin":  # macOS
            subprocess.run(["open", directory], check=True)
        else:  # Linux
            subprocess.run(["xdg-open", directory], check=True)

        return jsonify({'status': f'Explorer opened at {directory}'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
 # Flaskサーバーをデバッグモードで起動
    app.run(host='0.0.0.0', port=5000, debug=True)
