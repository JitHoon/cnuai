from crypt import methods
from flask import Flask, jsonify, request
# REST API 사용을 위해서 jsonify, request module을 불러온다.
# jsonify :  js 데이터 저장 방식으로 변환해주는 module
# request : HTTP module을 다룰 수 있는 module

# flask의 활성 모듈의 이름 __name__ 을 app으로 지정함
app = Flask(__name__)

myName = [
    {"id": 1, "name": "최"},
    {"id": 2, "name": "지"},
    {"id": 3, "name": "훈"}
]

# 웹 표현 method : route
# @ : decorator : 함수 장식자는 함수 코드를 바꾸지 않고도, 장식자 안의 내용만 바꿈으로 함수의 동작 조절 가능
# route decorator는 flask 서버로 '/' URL이 요청들어 왔을 때 밑에있는 함수를 호출함


@app.route('/')
def hello_flask():
    return "Welcome to Jit Hub"

# GET /myName | 자료를 가지고 온다


@app.route('/myName', methods=['GET'])
def get_myName():
    # 리스트는 json으로 변환될 수 없으므로 dic꼴로 바꾸고 jsonify module 사용
    return jsonify({"myName": myName})

# POST /myName | 자료를 /myName 자원에 추가한다


@app.route('/myName', methods=['POST'])
def create_menu():
    # 전달받은 자료를 menus 자원에 추가
    request_data = request.get_json()
    newName = {
        "id": 4, "name": request_data['name']
    }
    myName.append(newName)
    return jsonify(newName)


# 직접적인 실행파일로 사용될 때 run
if __name__ == '__main__':
    app.run()
