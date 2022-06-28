# 변수
from datetime import datetime
from math import remainder
from urllib import response

identity = 'identity'
print('변수', identity, '사용하기')

# 숫자, 연산식
my_age = 25
remainder = my_age ** 2

# 문자열
text = '2015' + '1991'
# 20151991 이라는 새로운 문자열 생성

# 조건문
if remainder > my_age:
    print('if문 참')
elif remainder > my_age:
    print('elif문 거짓')
else:
    print('else문 출력')


# 함수
def function(a):			# 함수의 정의
    print('[함수 정의 및  호출]', a, '[a는 매개인자]')
    c = '[반환 결과1]'
    d = '[반환 결과2]'
    return c, d


'''이건 주석'''

b = """[b는 실행인자]
'와 "도 사용가능"""
c, d = function(b)

print('함수는 여러 값을 출력 할 수 있다 {} {}' .format(c, d))

# 자료형 (정수, 실수)

print('실수는 값의 계산이 정확하지 않는 경우가 발생한다.')
print(0.1+0.1+0.1 == 0.3)  # False

# List 추가, 삭제, 검색
list1 = [1, 2, 3, 4]

del list1[0]     # 첫 번째 문자열 삭제
list1.remove(2)  # 숫자 2 삭제

list1.append(5)  # 문자열 뒤에 5 추가

n = 5

if n in list1:
    print('{}가 {}에 있다.'.format(n, list1))

# 반복문
names = ['철수', '영희', '영수']

for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))


# Module
def get_web(url):
    """URL을 넣으면 HTML을 반환하는 함수"""
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded


url = input('웹 페이지 주소?')
content = get_web(url)
print(content)

# Dictionary
