# ---- 라이브러리 입력 ----

# --- Framework : Flask / 웹 프레임워크. 백엔드 웹서버 역할을 함 ---
# -- feature : Flask --
# -- feature : jsonify --
# -- feature : request -- 

from flask import Flask, jsonify, request

# --- Library : pymongo / 몽고DB 데이터베이스 라이브러리. 파이썬에서 몽고DB와 연결한다
# -- feature : MongoClient
from pymongo import MongoClient

# --- Library : datetime / 시각, 날짜관련 라이브러리 ---
# -- feature : datetime
from datetime import datetime

# --- Library : flask_cors / HTTP CORS 오류 해결 라이브러리 ---
# -- feature : CORS
from flask_cors import CORS

# ---- 로컬 파일 임포트 ----

# --- Machine Learning : Segmentation
import model
# --- Machine Learning : Emotion Recognition
import emotion_sq


# ---- 서버 전체 참조 코드 ----

# --- Flask Initial Set Up ---
# -- 플라스크 서버를 기동하기 위한 초기 설정 : 플라스크 기능을 사용해 시동할 app 변수 만들기 --
app = Flask(__name__)

# --- CORS Access-Control-Allow-Origin Set Up ---
# -- 다른 포트의 프론트와 백엔드를 연결하는 과정에서 발생하는 CORS 에러를 해결하기 위한 코드 --
# -- Access-Control-Allow-Origin 값을 모든 곳에 보내주어 CORS 에러를 방지하기 (모든 곳에 보내주기 때문에 차후에는 변경해야함!) --
cors = CORS(app, resources={r"*": {"origins": "*"}})

# --- Pymongo Initial Set Up ---
# -- 데이터베이스 서버인 MongoDB와 웹 서버인 Flask 를 연결하기 위한 코드 --
# -- MongoClient 메서드를 사용하여 클라이언트의 이름과 포트번호를 정해준다 --
# -- 아래 코드는 로컬 환경에서 Robo,Studio 3T를 활용한 코드로, 몽고 클라우드 혹은 배포용 서버에서 사용하는 코드는 상이하다 --
client = MongoClient('localhost', 27017)
# - 선언한 클라이언트 변수의 컬렉션 이름을 정해주는 코드 --
db = client.chameleon



# ---- API : Initial frame ----
# --- 백엔드 서버 API에 진입할 때 필요한 코드 프레임. 실제 프로젝트에는 사용하지 않았음 ---

# 
@app.route('/')
def home():

    return jsonify ({'msg': 'success'})

# recent_selfie_id = str(db.selfie.find_one()['_id'])

@app.route('/loadimage', methods=['GET'])
def load_image():
    # -- 로직과 의사코드를 주석으로 달아보세요 --
    global recent_selfie_id
    print(f'최근 아이디 값은 : {recent_selfie_id}')
    gif_selfie_id = db.gif.find_one(
        {'selfie_id': recent_selfie_id})['selfie_id']
    print(f'이것은 셀피 아이디 값입니다 {gif_selfie_id}')
    if gif_selfie_id == recent_selfie_id:
        find_gif = db.gif.find_one()['name_gif']

        return jsonify({'find_gif': find_gif}, recent_selfie_id)

    # print(gif_selfie_id)
# load_image(recent_selfie_id)
# 1. 셀피 데이터를 먼저 print로 확인함
# 2. 셀피 데이터베이스에서 recent_selfie_id값을 정의해야함
# 3. 셀피 데이터베이스를 활용하여 이미지 gif를 가지고 와야함
# pass


#   --- 셀피 업로드하기 ---
@app.route('/saveselfie', methods=['POST'])
def save_selfie():
    # print('업로드로 들어오긴 합니까?')
    # print(request)
    # print(f'헤더에 오리진 들어옴? {request.headers}')
    # -- Request --
    file_receive = request.files['file_give']
    print(f'받아온 파일은 {request.files}')

    # -- API Progress --
    extension = file_receive.filename.split('.')[-1]
    print(f'extension {extension}')

    time_now = datetime.now()
    timestamp = f"{time_now.strftime('%Y%m%d_%H%M%S')}"

    global filename
    filename = f'{timestamp}.{extension}'
    print(f'filename : {filename}')

    save_to = f'static/image/selfie/{filename}'
    file_receive.save(save_to)

    doc_selfie = {
        'name_selfie': filename
    }

    db.selfie.insert_one(doc_selfie)
    model.make_gif(filename)

    global recent_selfie_id
    recent_selfie_id = str(db.selfie.find_one(
        {'name_selfie': filename})['_id'])
    print(f'최근 아이디 값은 : {recent_selfie_id}')

    # # -- Response --
    return jsonify({'save_to': save_to, 'recent_selfie_id': recent_selfie_id, 'filename': filename})
    # return redirect(url_for('save_gif')), recent_selfie_id, filename


@app.route('/savegif', methods=['POST'])
def save_gif():
    # --- Request ---
    data = request.form
    print(f'리퀘스트 폼 {data}')
    filename = request.form['filename']
    print(f'savegif : filename : {filename}')
    recent_selfie_id = request.form['recent_selfie_id']
    print(f'savegif : recent_id : {recent_selfie_id}')
    # --- Progress ---
    global current_time
    current_time = model.make_gif(filename)
    print(f'모델작동 {current_time}')

    gif_doc = {
        'selfie_id': recent_selfie_id,
        'name_gif': current_time
    }
    db.gif.insert_one(gif_doc)
    print('gif 데이터베이스 삽입')
    # --- Response ---

    return jsonify({'msg': 'gif를 저장했습니다!', 'current_time': current_time})


@app.route('/loadgif', methods=['GET'])
def result_gif():
    print(current_time, "1")

    return jsonify({'current_time': current_time})


@app.route('/emotion', methods=['GET'])
def load_emotion():
    # -- 감정 인식 함수 호출 --
    print('감정 인식 호출')
    global filename
    print(f'셀피 넣은 것 들어오나요   {filename}')
    # file = db.selfie.find_one({'name_selfie': filename})
    result = emotion_sq.find_emotion(filename)
    print(f'결과는 두구두구!   {result}')

    # -- 리스트 형식의 감정을 담음 --
    emotion = ['Angry', 'Disgust', 'Fear',
               'Happy', 'Sad', 'Surprise', 'Neutral']

    # -- result는 0~6 사이의 정수이므로 emotion list의 result를 대입해 감정을 빼낸다
    music_index = emotion[result]
    print(f'음악 이름 뭔가요! {music_index}')

    return jsonify({'music_index': music_index})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)