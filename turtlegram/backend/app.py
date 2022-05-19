import json
from socket import MsgFlag
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
    # print(request.form)
    # print(request.form.get('id'))
    # print(request.data)
    # print(request.data)

    # request
    data = json.loads(request.data)

    # api progress

    # 요청값 변수 담기
    id_receive = data.get('id')
    pw_receive = data.get('pw')

    # 비밀번호 암호화
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    # 아이디 일치여부 조회
    if db.user.find({'id': id_receive}):
        msg = '이미 존재하는 아이디입니다.'
    else:
        # 몽고디비 컬렉션 저장
        doc = {
            'id': id_receive,
            'pw': pw_hash
        }
        db.user.insert_one(doc)
        msg = '회원가입이 완료되었습니다.'
    return jsonify({'msg': msg})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
