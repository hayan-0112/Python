#p.254

#enumerate() 함수
#리스트 내부 요소를 반복문을 통해 출력할 때
#enumerate()를 사용해서 열거 순서를 반환 받을 수 있다.

lista=[3,2,1,4,6,5]
print(enumerate(lista))
#enumerate()를 호출하면 enumerate object (열거 객체)가 반환
print(list(enumerate(lista)))
#리스트를 enumerate()후 다시 list()로 형 변환 시
#리스트의 요소별 인덱스 번호와 요소의 값을 튜플형태로 얻을 수 있다.
# => [(0, 3), (1, 2), (2, 1), (3, 4), (4, 6), (5, 5)]

#for문과 사용 예
for idx, value in enumerate(lista):
    print("{}번째 요소의 값: {}".format(idx, value))

#이터러블 / 이터레이터
#반복할 수 있는 것 : 이터러블(interable)
#반복가능 객체 : 이터러블 객체 ex) list, 문자열, enum 객체 등
#이터러블은 내부에 있는 요소를 차례로 꺼낼 수 있는 객체

#이터러블에서 next()함수를 통해 하나씩 꺼낼 수 있는 요소를
#이터레이터라고 한다.

numbers=[1,2,3,4,5,6]
print(id(numbers), "list의 주소")
print(id(numbers[0]))
print(id(numbers[1]))
print(id(numbers[2]))
print(id(numbers[3]))
print(id(numbers[4]))
print(id(numbers[5]))

r_num = reversed(numbers)
print(r_num) # reversed 함수의 반환 값 : reverseiterator 객체

#위 reverseiterator 같은 이터러블 객체를 대상으로 next()함수를 적용
print(next(r_num)) #6출력
print(next(r_num)) #5
print(next(r_num)) #4
print(next(r_num)) #3
print(next(r_num)) #2
print(next(r_num)) #1

#반복문 for를 사용하지 않고 next함수를 통해 차례로 하나씩 값 호출 가능

# -5 ~ 256 까지의 정수는 파이썬 메모리에 기본 할당

listb = [1,2,3,4,1,2,3,4,1,2,3] #숫자 리스트 선언
counter = {} #숫자별 개수 저장하기 위한 빈 딕셔너리 선언

for b in listb: #숫자를 하나씩 꺼내서
    if b not in counter: #딕셔너리에 해당 숫자 키가 없다면
        counter[b] = 0 #해당 숫자 키에 0 할당
    counter[b] += 1 #해당 숫자 키 카운트를 1 올림

print("{}에서\n 사용된 숫자의 종류는 {}개입니다.".format(listb, len(counter))) #출력
print("참고: {}".format(counter))

#p.268_2번
# ctacaatgtcagtatacccattgcattagccgg
#각 요소마다 몇 개가 있는지 카운트하는 문제
#1번문제와 동일하게 접근
str = "ctacaatgtcagtatacccattgcattagccgg"
counter = {}

for s in str: #74~77까지는 1번문제와 동일
    if s not in counter:
        counter[s] = 0
    counter[s] += 1

for key in counter: #출력방식만 1번문제와 다름
    print("{}의 개수: {}".format(key, counter[key]))

#p.269_3번
str = "ctacaatgtcagtatacccattgcattagccgg"
for i in range(0, len(str), 3): #0부터 str의 길이까지 3스텝
    sliced = str[i:i+3] #for문 첫 바퀴의 경우 i=0, 0~3까지 슬라이싱
    if len(sliced) == 3: #슬라이싱 한 결과가 len 값 3이면 출력
        print(sliced)

#p.270 리스트 평탄화 flatten
#중첩된 리스트를 1차원으로 평탄화하는 문제, 모든 중첩을 제거
l = [1,2,[3,4],5,[6,7],[8,9]]
res = [] #평탄화된 리스트를 담기 위한 빈 리스트 선언
for i in l: #원본 리스트에서 요소 하나씩 반복
    if type(i) == list: #i를 통해 꺼낸 요소의 타입이 리스트라면
        for j in i: #list를 다시 반복문으로 j를 통해 요소 하나씩
            res.append(j) #꺼낸 j요소를 res 리스트에 append
    else: #i를 통해 꺼낸 요소의 타임이 리스트가 아닌 경우
        res.append(i) #바로 res에 추가
print("{}를 평탄화 하면 {}입니다.".format(l,res)) #출력


listc = [1,2,3,4]
x = len(listc)
print(x)

#함수 function, method

#함수의 호출 = 함수의 사용 = call = ()
#함수의 매개변수
#함수의 리턴 = 함수의 변환 = 함수의 결과

#함수의 기본 형태
#def키워드를 사용한다

def myfunc(): #함수의 정의
    print("함수 실행문1") #함수 내부 설명문
    print("함수 실행문2")
    print("함수 실행문3")
    print("함수 실행문4")

myfunc() #함수의 호출
dict={"a":1}
print(myfunc)
print(dict.keys())

#매개변수 : 함수의 정의 측면에서 용어
#매개변수 : 함수에서 요구하는 재료 변수

print(locals(), "local1")
def myfunc2(mV, nV):
    print(id(mV))
    print(id(nV))
    print(id(mV+nV))
    print(locals(), "local2")
    locals()['xx'] = 10
    print(locals(), "local3")

print(locals(),"local4")
myfunc2(128,129)
#print(a) 함수의 매개변수는 함수 내에서만 유효하다

#parameter : 매개변수(함수의 호출에서 전달한 값을 정의에서 받는 변수)
#argument : 전달인자 (함수 호출 시점에서 정의로 전달하는 값)

#가변 매개변수 *
#가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
#가변 매개변수는 하나만 사용 가능
def myfunc3(a,b,*c):
    print(a,b,c)

myfunc3(1,2,3)

def print_n_times(n, *values):
    #n번 반복합니다.
    for i in range(n):
        #values는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순한 줄바꿈
        print()

#함수를 호출합니다.
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

#기본 매개변수
#매개변수 = 값 형태
#기본 매개변수는 기본 값을 가짐
#따라서 안 써도 되고 써도 되고
#default 값이 있음
print("첫번째줄",1,300, sep = '_', end='.', flush="False")
print("두번째줄")

#기본
print()

def print_n_tims(value, n=2):
    #n번 반복합니다.
    for i in range(n):
        print(value)
#함수를 호출합니다.
print_n_tims("안녕하세요")

#리턴 return
#어떤 함수는 원본을 바꾸고
#어떤 함수는 원본을 바꾸지 않고
#어떤 함수는 리턴값이 있고
#혹은 없고

a = "hello"
a.replace('h','!')
print(a) #원본에서 바뀌지 않음<원본 유지>
a.upper()
print(a) #원본에서 바뀌지 않음<원본 유지>
a.strip()
print(a) #원본에서 바뀌지 않음<원본 유지>

print(a.replace('h','!')) # 바뀜
print(a.upper())
print(a.strip())

b=[1,2]
print(b.append(3)) #None이 나오는 것 : return이 없는 것
print(b)

def rt():
    print(1)
    return 100
    print(2)

rt()
print(rt())


#return은 함수 내에 작성 가능
#함수 내에서 return 키워드가 읽히면 함수를 탈출한다.
#return 뒤에 작성 된 value를 들고 탈출함
#return 뒤에 value가 없으면 None 반환

#범위 내부의 정수를 모두 더하는 함수
# 함수를 선언합니다.
def sum_all(start, end):
    # 변수를 선언합니다.
    output = 0
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1):
        output += i
    # 리턴합니다.
    return output

# 함수를 호출합니다.
print("0 to 100: ", sum_all(0,100))
print("0 to 1000: ", sum_all(0,1000))
print("50 to 100: ", sum_all(50,100))
print("50 to 1000: ", sum_all(50,1000))

#기본 매개변수와 키워드 매개변수를 활용해 범위의 정수를 더하는 함수
# 함수를 선언합니다.
def sum_all(start=0, end=100, step=1):
    # 변수를 선언합니다.
    output = 0
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1, step):
        output += i
    # 리턴합니다.
    return output

# 함수를 호출합니다.
print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end = 100))
print("C.", sum_all(end = 100, step = 2))

def f(x):
    return (2*x)+1
print(f(10))

def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output

print(mul(5,7,9,10))