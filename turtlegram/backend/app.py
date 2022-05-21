import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import hashlib


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

client = MongoClient('localhost', 27017)
db = client.nabacamp


@app.route('/')
def hello_world():
    return jsonify({'message': 'success'})


@app.route('/signup', methods=['POST'])
def sign_up():
    data = json.loads(request.data)

    id_receive = data.get('id')
    pw_receive = data.get('pw')

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    if db.user.find({'id': id_receive}):
        msg = '이미 존재하는 아이디입니다.'
    else:
        doc = {
            'id': id_receive,
            'pw': pw_hash
        }
        db.user.insert_one(doc)
        msg = '회원가입이 완료되었습니다.'
    return jsonify({'msg': msg})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
