from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        a = int(request.args.get('a', 0))
        b = int(request.args.get('b', 0))
        return jsonify({'result': a + b})
    except (TypeError, ValueError):
        return jsonify({'error': '参数错误，a 和 b 应该是整数'}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False)
