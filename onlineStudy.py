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

'''
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
'''

# Dictionary
wintable = {
    '가위': '보',
    '바위': '가위',
    '보': '바위',
}

for a in wintable.items():
    print('{}는 {}를 이김'.format(*a))

d = {}
d['a'] = 1
print(d)

1 in d    # False
'a' in d  # True

# 형변환
str(1)
int('1')
list({1, 2, 3})
set([1, 2, 3])

# packing, unpacking
c = (3, 4)
d, e = c        # unpacking
f = d, e        # packing

d, e = e, d     # 값 서로 바꾸기
print(d, e)

# while, break, continue
selected = None

while selected not in ['가위', '바위', '보']:
    selected = input('가위, 바위, 보, n 중에 선택하세요 : ')

    if selected == 'n':
        break

print(selected)

list = range(4)


for i in list:
    if i % 2 == 0:
        continue
    print(i)

money = 0
salary = 2000_0000
year = 0

while money < 5_0000_0000:
    money = money + salary
    year = year + 1
    salary = salary * 1.1

print(year)

# try, except

# 에러 관리
# 에러 이름을 알 때


def errorfunc(list, index):
    try:
        print(list.pop(index))
    except IndexError:
        print('{} index를 가져올 수 없습니다.'.format(index))


errorfunc([1, 2, 3], 5)

# 에러 이름을 모를 때
'''try:
    a = 5
    b = 0
    c = a / b
except Exception as a:
    print('다음과 같은 에러가 발생했습니다: {}'.format(a))
'''

# slice
list1 = [0, 1, 2, 3, 4, 5]
list1[1:4] = [11, 22, 33]

list2 = [0, 1, 2, 3, 4, 5]
del list2[1:3]

print("list1 : {}, list2 : {}".format(list1, list2))

# List Comprehension
list1 = [i*i for i in range(1, 11)]  # [ 계산식 for문 ]`
list2 = [i*i for i in range(1, 11) if i % 2 == 0]  # [ 계산식 for문 조건문 ]`
list3 = [(x, y) for x in range(3) for y in range(3)]  # [ 계산식 for문 for문 ]`

print(list1)
print(list2)
print(list3)

# Dictionary Comprehension

scores = [100, 89, 75]
students = ['지훈', '짓훈', '징훈']


dic1 = {"{}".format(number): scores for scores, number in enumerate(students)}

dic2 = {student: score for student, score in zip(students, scores)}

print(dic1)
print(dic2)

# 날짜, 시간 함수 다루기
'''


def days_until_christmas():
    christmas_2030 = datetime.datetime(2030, 12, 25)
    days = christmas_2030 - datetime.datetime.now()
    return days.days


print("{}일".format(days_until_christmas()))
'''

'''undred_after가 지금으로부터 100일 후,
9시 정각을 값으로 가지는 datetime클래스의 인스턴스가 되도록 만들어 보세요. '''

'''
hundred_after = datetime.datetime.now().replace(
    hour=9, minute=0, second=0) + datetime.timedelta(days=100)

print("{}/{}/{}  {}:{}:{}".format(hundred_after.year, hundred_after.month,
      hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))
'''
# clsaa, inheritance


class Animal():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print("걷는다")

    def eat(self):
        print("먹는다")

    def greet(self):
        print("super()를 사용하여 부모 내용을 추가하여 {}이/가 인사한다".format(self.name))


class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name)  # 부모클래스의 __init__ 메소드 호출
        self.hand = hand

    def wave(self):
        print("{}을 흔들면서".format(self.hand))

    def greet(self):
        self.wave()
        super().greet()


class Dog(Animal):

    def wag(self):
        print("꼬리를 흔든다")

    def greet(self):
        self.wag()


person = Human("사람", "오른손")
person.greet()

dog = Dog("강아지")

person.walk()
person.eat()
person.wave()
dog.walk()
dog.eat()
dog.wag()

# override (부모의 greet를 출력하지 않고 본인의 greet를 덮어씀)
person.greet()
dog.greet()


# 사용자 예외


class PasswordNotMatched(Exception):
    print("Exception을 상속 받는 BadUserName 클래스이며 용도는 error 예외 입니다.")


def sign_up():
    print("회원가입하는 함수")


try:
    sign_up()
except PasswordNotMatched:
    print("입력한 패스워드 불일치")

'''
import pandas

데이터 프레임

column : 세로 데이터
info() : 
describe() : 특성의 분포

kaggle
데이콘
quickdraw
.
'''
