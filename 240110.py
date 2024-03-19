#재귀함수
#일부 반복문으로 대체 가능
#Recursion / Recursive
#def myfunc():
#함수가 자기 자신을 다시 호출하는 함수

# f(x) = 2x + 1 ---> 일반적인 함수
# 팩토리얼
# n!
# n! = n * (n-1) * (n-2) --- * 1

# 반복문으로 팩토리얼 구하기
def fac(n):
    output = 1
    for i in range(1, n+1):  # 1부터 n+1까지의 범위
        output *= i # output = output * i
    return output

print("1!:", fac(1))
print("2!:", fac(2))
print("3!:", fac(3))
print("4!:", fac(4))
print("5!:", fac(5))
print(fac(50))

#재귀함수로 팩토리얼 함수 돌리기 -> fac(n) = n * fac(n-1)
def fac2(n):
    if n==0:
        return 1
    else:
        return n*fac2(n-1)
print(fac2(3))

d1={"1":{"1":{"1":{"1":100000}}}} #재귀적으로 들어감
d2={"1":2000} #재귀적으로 들어가지 않음
def show(dic):
    if type(dic['1']) != int: #정수가 아닐 때
        show(dic['1'])
    else: #정수일 때
        print(dic['1'])
show(d1)
show(d2)

a = [[1,2,3],[4,[5,6]],7,[8,9]]
print(len(a))
(print(a[0]))
print(a[0])
print(a[1])
print(a[2])
print(a[3])

def flatten(data):
    output = []
    for item in data:
        if type(item) == list:
            output += item
        else:
            output.append(item)
    return output
a = [[1,2,3],[4,[5,6]],7,[8,9]]
print(flatten(a))

def flatten2(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flatten2(item) #1,2,3,4,5,6,8,9  --> list 타입
        else:
            output.append(item) #7 --> 그냥 숫자<붙힘>
    return output
a = [[1,2,3],[4,[5,6]],7,[8,9]]
print(flatten2(a))

min_person = 2
max_person = 10
total_person = 100
memo = {}

def table(stand, set):
    key = str([stand, set])
    # 종료 조건
    if key in memo:
        return memo[key]
    if stand < 0:
        return 0
    if stand == 0:
        return 1
    #재귀 처리
    count = 0
    for i in range(set, max_person + 1):
        count += table(stand-i, i)
    #메모리 처리
    memo[key] = count
    #종료
    return count