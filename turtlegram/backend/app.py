import json, jwt
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta


app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

SECRET_KEY = 'WIZARD1993'

client = MongoClient('localhost', 27017)
db = client.turtlegram

app.config['SECRET_KEY'] = SECRET_KEY
app.config['BCRYPT_LEVEL'] = 10
bcrypt = Bcrypt(app)



@app.route('/')
def hello_world():
    return jsonify({'message': 'success'})


@app.route('/signup', methods=['GET','POST'])
def sign_up():
    if request.method =='POST':
        data = json.loads(request.data)

        print(f'리퀘스트 데이터 체크 {data}')

        id_receive = data['email']
        pw_receive = data['password']

        print(f'리퀘스트 변수 체크 id{id_receive}, pw{pw_receive}')

        pw_hash = bcrypt.generate_password_hash(pw_receive)

        # -- 이메일 조회 --
        if '@' in id_receive:
            if '.' in id_receive.split('@'):
                # -- 중복 조회 --
                if db.user.find_one({'id': id_receive}):
                    doc = {
                        'id': id_receive,
                        'pw': pw_hash
                    }
                    db.user.insert_one(doc)
                    msg = '회원가입이 완료되었습니다.'
                    print(msg)
                    return jsonify({'msg': msg}), 201
                    
                else:
                    msg = '이미 존재하는 아이디입니다.'
                    print(msg)
                    return jsonify({'msg': msg}), 203
            else:
                msg = '이메일 형식이 아닙니다.'
                print(msg)
                return jsonify({'msg': msg}), 202
        else:
            msg = '이메일 형식이 아닙니다'
            print(msg)
            return jsonify({'msg': msg}), 202

        
        

@app.route('/login', methods=['POST'])
def sign_in():
    # --- request ---
    data = json.loads(request.data)

    # --- progress ---
    id_receive = data.get('id')
    pw_receive = data.get('pw')

    
    find_user = db.user.find_one({'id': id_receive})

    if find_user:
        # -- pw check --
        if bcrypt.check_password_hash(find_user['pw'],pw_receive):
            # -- payload --
            payload = {
                'id': find_user['id'],
                'exp' : datetime.utcnow() + timedelta(seconds=60*60*2)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            return jsonify ({'token': token})
        else:
            msg = '비밀번호가 일치하지 않습니다.'
    else:
        msg = '존재하지 않는 아이디입니다.'

    # --- response --- 



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
