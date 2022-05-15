import json
from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/')
def hello_world():
    return jsonify({'message': 'success'})


@app.route('/signup', methods=['POST'])
def sign_up():
    # print(request.form)
    # print(request.form.get('id'))
    # print(request.data)
    data = json.loads(request.data)
    print(f'data={data}')
    print(data.get('email'))
    print(data.get('password'))
    return jsonify({'msg': 'True'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
