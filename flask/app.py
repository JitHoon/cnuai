from flask import Flask

# flask의 활성 모듈의 이름 __name__ 을 app으로 지정함
app = Flask(__name__)

# 웹 표현 method : route
# @ : decorator : 함수 장식자는 함수 코드를 바꾸지 않고도, 장식자 안의 내용만 바꿈으로 함수의 동작 조절 가능
# route decorator는 flask 서버로 '/' URL이 요청들어 왔을 때 밑에있는 함수를 호출함.


@app.route('/')
def hello_flask():
    return "Welcome to Jit Hub"


# 직접적인 실행파일로 사용될 때 run
if __name__ == '__main__':
    app.run()
