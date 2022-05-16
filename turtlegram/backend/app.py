import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient


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
    data = json.loads(request.data)
    id_receive = data.get('id')
    pw_receive = data.get('pw')
    # print(f'data={data}')
    doc = {
        'id': id_receive,
        'pw': pw_receive
    }
    db.user.insert_one(doc)
    return jsonify({'msg': 'True'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
