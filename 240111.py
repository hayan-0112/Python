#튜플
#괄호가 없는 튜플
#만들면
#return 으로 반환 받는 형태로 튜플이 많이 쓰임
def xxx():
    return

tp = 10,20,30,40
print(tp)

a,b = 10,20
print(a)
print(b)
a,b=b,a
print(a)
print(b)

#람다 lambda 표현
#함수의 표현법 중 하나

def xxxx(): #사용자 함수를 정의 함
    print("xxxx함수가 호출되었다.")
#람다 : 코드 중간에 정의와 호출을 하는 방법
#호출 부분은 따로 존재
xxxx()

#매개변수로 받은 함수를 10번 호출하는 함수
def call_10_times(func):
    for i in range(10):
        func()
#간단한 출력하는 함수
def print_hello():
    print("안녕하세요")
#조합하기
call_10_times(print_hello) #콜백함수 사용 방법
#콜백함수 : 함수의 매개변수에 사용되는 함수
#콜백함수 : 함수() 이 아니라 함수의 명 전달
print(print_hello)
print(id(print_hello), "-> print hello함수의 메모리")

def play(func):
    for i in range(10):
        func()
def a():
    print("a")
def b():
    print("b")
def c():
    print("c")
play(a)

#filter 함수
#map 함수
#함수를 매개변수로 사용하는 대표적인 함수들
#map(함수명, 리스트) : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트 구성
#filter(함수명, 리스트) : 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트 구성

#람다 : 코드 중간에 정의와 호출을 하는 방법
#def를 사용하지 않는다.(정의 단계가 없다)
#함수를 간단하게 선언하는 방법

power = lambda x: x * x
under_3 = lambda x: x < 3


#함수를 선언합니다.
def power(item):
    return item * item
def under_3(item):
    return item < 3

#변수를 선언합니다.
list_input_a = [1,2,3,4,5]

#map() 함수를 사용합니다.
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a): ", output_a)
print("map(power, list_input_a): ", list(output_a))
print()

#filter() 함수를 사용합니다.
output_b = filter(under_3, list_input_a)
print("# filter() 함수의 실행 결과")
print("filter(under_3, list_input_a): ", output_b)
print("filter(under_3, list_input_a): ", list(output_b))

#filter object와 map object는 제너레이터라고 한다.
#메모리 절약을 위해서 제너레이터 object형태로 반환이 온다.
#제너레이터 내부 값을 조회하려면 list로 형 변환

#일반 함수(사용자 정의 def)
#재귀 함수:
#   1. 탈출 조건이 있어야 함
#   2. 문제 해결 방법이 동일
#콜백 함수

#람다 : 코드 중간에 정의와 호출을 하는 방법
#def를 사용하지 않는다.(정의 단계가 없다)
#함수를 간단하게 선언하는 방법

power = lambda x: x * x
under_3 = lambda x: x < 3

a = map(power,[1,2,3,4,5]) #람다식을 제대로 쓴 게 x
a = map(lambda x: x * x, [1,2,3,4,5]) #람다식을 제대로 쓴 것. 람다식을 중간에 정의 및 사용하는 것 --> 람다식
print(a)
print(list(a))

#람다 사용 장점: 미리 선언되지 않은 함수를 중간에 선언 가능
#람다 사용 단점: 간단한 return 방식의 함수 구성만 가능

#파일 처리
#파일 관련 처리 내장 함수

#파일 열기 함수 open
#파일 읽기 함수 read
#파일 쓰기 함수 write
#파일 닫기 함수 close

#open()  -> open(경로, mode)
#파일 오픈 함수의 매개변수
#1. 파일 경로 : 파일 경로는 문자열로 처리
#2. 파일 오픈 모드
#   2.1 오픈 모드 w : write 모드(새로쓰기)
#   2.2 오픈 모드 a : append모드(이어쓰기)
#   2.3 오픈 모드 r : read모드(읽기)

file = open("basic.txt", 'w')
file.write("hello python")
file.write("hello python")
file.write("hello python")
file.writelines("hello python")
file.write("hello python")
file.write("hello python")
file.write("hello python")
file.write("hello python")
file.write("hello python")
file.close()
#파일을 열면 항상 닫아줘야 한다.
#파일이 중복으로 열리면 생기는 문제 방지

#with 방식으로 파일을 여는 방법

with open("basic.txt", 'w') as f:
    f.write("hello")
    f.write("hello")
    f.write("hello")
    f.write("hello")

#with open() as f : 방식으로 파일을 오픈하면 close를 생략 가능

#텍스트 읽기
#reaD()
with open("basic.txt", 'r') as f1:
    contents=f1.read()
print(contents)

#텍스트 한 줄씩 읽기
#데이터를 구조적으로 표현하는 방식 CSV, JSON, XML
#ex) CSV
#이름, 키, 몸무게
#A , 170, 70
#B , 160, 60

#CSV 파일은 한 줄에 하나의 데이터
#쉼표로 데이터 구분
#첫 줄은 데이터의 헤더(헤더는 데이터가 무엇을 나타내는지)

#랜덤한 숫자를 만들기 위해 가져옵니다.
import random #random
#간단한 한글 리스트를 만듭니다.
hanguls = list("가나다라마바사아자차카타파하")
#파일을 쓰기 모드로 엽니다.
with open("info.csv",'w') as file:
    file.write("{}, {}, {}\n".format("이름", "체중", "신장"))
    for i in range(1000):
        #랜덤한 값으로 변수를 생성합니다.
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140,200)
        #텍스트를 씁니다.
        file.write("{}, {}, {}\n".format(name, weight, height))

# with open("info.txt", "r") as file:
#     for line in file:
#         # 변수를 선언합니다.
#         (name, weight, height) = line.strip().split(", ") #strip() : 혹시나 있을 양쪽의 공백을 제거, #split() : 파일 정돈
#
#         # 데이터가 문제없는지 확인합니다: 문제가 있으면 지나감
#         if (not name) or (not weight) or (not height):
#             continue
#
#         # 결과를 계산합니다.
#         bmi = int(weight) / ((int(height) / 100) ** 2)
#         result = ""
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상 체중"
#         else:
#             result = "저체중"
#
#         # 출력합니다.
#         print('\n'.join([
#             "이름: {}",
#             "몸무게: {}",
#             "키: {}",
#             "BMI: {}",
#             "결과: {}"
#         ]).format(name, weight, height, bmi, result))
#         print()

c = 0
def hanoi(circle, start, end, middle):
    #A B C
    global c
    c += 1
    if circle == 1:
        print(start, '->', end)
        return
    if circle >= 2:
        #아래의 원판을 제외하고, 시작 기둥에서 보조 기둥으로 이동한다.
        hanoi(circle - 1, start, middle, end)
            #A C B #가장 아래를 제외한 모든 원판 내려놓기
        print(start, '->', end) #최하단 원판 옮기기 : 1회
        #아래의 원판을 제외하고, 보조 기둥에서 대상 기둥으로 이동한다.
        hanoi(circle - 1, middle, end, start)
            #C B A #가장 아래 원판 제외한 내려놓은 원판을
            #가장 아래원판의 위에 올리기
        #count = 2 ** n - 1

n = int(input("원판의 개수를 입력하세요: "))
hanoi(n, "A탑", "B탑", "C탑")
print(f"이동 횟수는 {c}회입니다.")