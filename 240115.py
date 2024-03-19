#예외처리
#구문오류

#index
#value
#type
#syntax

#=> 프로세스가 강제 멈춤


stra = "123456789"
print(stra.find('0'))
#print(stra.index('0'))
#find는 찾는 문자가 없다면 -1을 리턴한다.
#index는 찾는 문자가 없다면 오류 발생

while 1:
    try:
        x = input("1~9중 숫자 입력: ")
        stra = "123456789"
        print(stra.index(x))
    except: #예외일 때 실행되는 코드
        print("error")
    break

#lista = [1,2,3,4,5,6,7,8,9]
#print(lista.index(0))

#변수를 선언합니다.
list_input_a = ["52", "273", "32", "스파이", "103"]

#반복을 적용합니다.
list_number = []
for item in list_input_a:
    #숫자를 변환해서 리스트에 추가합니다.
    try:
        float(item) #예외가 발생하면 알아서 다음으로 진행은 안 되겠지?
        list_number.append(item) #예외 없이 통과했으면 list_number 리스트에 넣어줘!
    except:
        pass

#출력합니다.
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))

#try except else
#try : 시도 실행 코드
#execpt : 예외 발생 코드
#else : 예외가 없이 실행 되었을 때 코드

try:
    x = int(input("숫자입력: "))
except:
    print("오류발생 o")
else: #try의 모든 코드가 정상실행 조건
    print("오류발생 x")


#finally
#finally는 예외 처리 구문에서 가장 마지막에 사용하는 구문
#예외발생이 있든 없든 무조건 실행한다.

try:
    x = int(input("num input"))
except:
    print("예외발생")
else:
    print("정상실행")
finally:
    print("항상 실행하는 코드")

#try except 구문으로 예외를 처리합니다.
try:
    #숫자로 변환합니다.
    number_input_a = int(input("정수 입력> "))
    #출력합니다.
    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2*3.14*number_input_a)
    print("원의 넓이: ", 3.14*number_input_a*number_input_a)
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")

#try는 단독 사용 불가, except 혹은 finally를 같이 사용
#else는 except 뒤에 위치

#try+exc
#try+fianlly
#try+exc+finally
#try+exc+else+finally
#try+exc+else

#try except 구문을 사용합니다
try:
    #파일을 엽니다.
    file = open("info.txt", "w")
    #여러 가지 처리를 수행합니다.
    예외.발생하라()
    #파일을 닫습니다.
    file.close()
except:
    print("오류가 발생했습니다.")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed: ", file.closed)


#test() 함수를 선언합니다.
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

#test() 함수를 호출합니다.
test()

#함수 내부에 try finally 구조 있으면
#try 도중 return해도 finally 실행 후
#탈출한다.
#반복문의 break 경우에도 마찬가지로
#finally구문을 실행하고 탈출한다.

while True:
    try:
        print("1")
        break
        print("2")
    except:
        print("exc")
    finally:
        print("final")

try:
    file = open("202dfsfsfds.txt", "r")
except Exception as e:
    print(e)
else:
    file.close()

    print("파일 닫혔는지 확인")
    print(file.closed)

#예외객체 excetpion object
#예외객체는 예외정보를 담고 있다.
#모든 종류의 예외정보를 담고 있는 Exception 예외 객체를 보통 사용
#Exception 은 클래스

try:
    x = int(input("숫자입력"))
except Exception as exc:
    print(exc)
    print(type(exc))

#변수를 선언합니다.
list_number = [52, 273, 32, 72, 100]

#try except 구문으로 예외를 처리합니다.
try:
    #숫자를 입력받습니다.
    number_input = int(input("정수 입력> "))
    #리스트의 요소를 출력합니다.
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except Exception as exception:
    #예외 객체를 출력해봅니다.
    print("type(exception): ", type(exception))
    print("exception: ", exception)

try:
    number_input = int(input("정수 입력>> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except IndexError as e:
    print("인덱스 범위 오류", e)
except ValueError as e:
    print("정수 입력하세요", e)
except Exception as e:
    print(e)


#raise 구문

# number = input("정수입력")
# number = int(number)
# if number > 0:
#     raise NotImplementedError
# else:
#     raise NotImplementedError

#raise 강제 에러 발생
#raise 예외 객체

#표준모듈 : 내장 1. datetime 2. random
#외부모듈 : 다운로드 설치

#표준모듈 1. Math
import math

print(math.floor(2.5)) #내림
print(math.ceil(2.5)) #올림

print(round(3.3))

from math import sin, cos, tan, floor

#from 방식으로 모듈 import하면
#모듈명. 을 생략 가능
#sin()

import random
print("# random 모듈")

#random() : 0.0 <= x < 1.0 사이의 float를 리턴합니다.
print("-random(): ", random.random())

#uniform(min, max) : 지정한 범위 사이의 float를 리턴합니다.
print("- uniform(10, 20): ", random.uniform(10, 20))

#randrange(): 지정한 범위 사이의 int를 리턴합니다.
#- randrange(max) : 0부터 max 사이의 값을 리턴합니다.
#- randrange(min, max) : min부터 max 사이의 값을 리턴합니다.
print("- randrange(10): ", random.randrange(10))

#choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
print("- choice([1,2,3,4,5]): ", random.choice([1,2,3,4,5]))

#shuffle(list) : 리스트의 요소들을 랜덤하게 섞습니다.
print("- shuffle([1,2,3,4,5]): ", random.shuffle([1,2,3,4,5]))

#sample(list, k=<숫자>) : 리스트의 요소 중에 k개를 뽑습니다.
print("- sample([1,2,3,4,5] , k=2): ", random.sample([1,2,3,4,5], k=2))

#random
#random() : 0.0 <= ~ < 1.0 사이 float
#uniform(n,m) : n~m 사이 균등분포 값
#randrange(10) : 0부터 10사이 값 리턴
#randrange(10,20) : 10~20 사이 리턴
#choice([리스트]) 리스트에서 랜덤 선택
#shuflle([리스트]) 리스트 섞기
#sample (list, k=x) 리스트에서 k에 지정한 x개 만큼 뽑기

sum = 0
n = int(input("몇 번"))

for i in range(n):
    uni = random.uniform(0,10)
    sum += uni
    print(sum/n)

#모듈을 읽어 들입니다.
import sys

#명령 매개변수를 출력합니다.
print(sys.argv)
print("---")

#컴퓨터 환경과 관련된 정보를 출력합니다.
print("getwindowsversion:()", sys.getwindowsversion())
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

#프로그램을 강제로 종료합니다.
#sys.exit()

import os

#기본 정보를 몇 개 출력해 봅시다.
print("현재 운영체제: ", os.name)
print("현재 폴더: ", os.getcwd())
print("현재 폴더 내부의 요소: ", os.listdir())

#폴더를 만들고 제거합니다.(폴더가 비어있을 때만 제거 가능).
os.mkdir("hello")
os.rmdir("hello")

#파일을 생성하고 + 파일 이름을 변경합니다.
with open("orginal.txt", "w") as file:
    file.write("hello")
os.rename("orginal.txt", "new.txt")

#파일을 제거합니다.
os.remove("new.txt")
#os.unlink("new.txt")

#시스템 명령어 실행
os.system("dir")

#p. 412
#모듈을 읽어 들입니다.
import datetime

#현재 시각을 구하고 출력하기
print("#현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

#시간 출력 방법
print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,\
                                            now.month,\
                                            now.day,\
                                            now.hour,\
                                            now.minute,\
                                            now.second)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(*"년월일시분초") #문자열, 리스트 등 앞에 *을 붙이면 요소 하나하나가 매개변수로 지정된다.
print(output_a)
print(output_b)
print(output_c)
print()

import time

for i in "hello":
    time.sleep(2)
    print(i)

from urllib import request
target = request.urlopen("http://image.dongascience.com/Photo/2020/03/5bddba7b6574b95d37b6079c199d7101.jpg")
output = target.read()
print(output)

file = open('output.png', 'wb')
file.write(output)
file.close()
#b' 데이터~~~~~~~~~~~~
#바이너리 데이터
#텍스트 데이터 100
#텍스트 100이라는 숫자는 1,0,0으로 구성
#텍스트 데이터 100은 49 48 48
