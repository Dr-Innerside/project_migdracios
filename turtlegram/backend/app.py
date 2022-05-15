import json
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({'message': 'success'})


@app.route('/signup', methods=['POST'])
def sign_up():
    print(request.form)
    print(request.form.get('id'))
    print(request.data)
    data = json.loads(request.data)
    print(data)
    return jsonify({'msg': 'True'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
