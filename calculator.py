#연봉계산기

#근로소득간이세액표의 월급여는 천원단위이며,
#이상, 미만으로 구간이 설정되어 있음.
#사용자 input 입력 사항
#1.연봉(원단위)
#2.비과세액(원단위)
#3.부양가족수(본인포함), 최소:1 최대:11

#결과 출력 사항
#1.국민연금(4.5%)
#2.건강보험(3.545%)
#3.요양보험:건강보험의 12.95%
#4.고용보험(0.9%)
#5.근로소득세(표참고)
#6.지방소득세:근로소득세의 10%
#7.년 예상 실수령액(원단위)
#8.월 환산 실수령액(원단위)
#*모든 단계에서 1원단위는 절사 0으로 치환

#6500구간 부양가족 6명: 값 없음
#   1. 근접 인덱스 값 존재 여부 체크
#   2. 근접 인덱스 값을 통한 예측값 계산
#6500구간 부양가족 11명 값 변경
#   1. 모든 인덱스의 값에 대한 연속성 체크
#6800구간 부양가족 5명 6명 연속 값 0
#   1. 연속 인덱스 값 오류의 경우 더 넓은 범위의 커널 설정
#6980구간 부양 1명 값 알파벳
#   1. 모든 인덱스의 값의 자리 수 체크 및 isdigit 검토


def public(year):
    result = int(year * 0.045 / 12)
    print('국민연금: {:,}원'.format(result))

def health(year):
    result = int((year * 0.03545) / 12)
    print('건강보험: {:,}원'.format(result))

def convale(health):
    result = int(health * 0.1295)
    print('요양보험: {:,}원'.format(result))

def employ(year):
    result = int(year * 0.009 / 12)
    print('고용보험: {:,}원'.format(result))


with open('2023.txt', 'r') as file:
    temp = {} #빈 딕셔너리 선언
    for idx, i  in enumerate(file): #파일의 모든 라인에 대한 반복
        split_i = i.split('\t') #개별 라인에 대한 split으로 \t를 기준으로 리스트화
        temp[idx] = split_i #딕셔너리의 0번키부터 위 split된 리스트를 value로 추가
    for i in temp:#딕셔너리의 모든 키에 대한 반복
        for idx, j in enumerate(temp[i]): #딕셔너리의 모든 키에 대한 value에 대한 반복
            temp[i][idx] = temp[i][idx].strip() #딕셔너리 value의 리스트 내부 모든 요소에 대한 공백제거
            temp[i][idx] = temp[i][idx].replace(",","") #쉼표 제거
            if "\n" in j: #\n이 나오면 split 후 앞에 것만 살리는 작업
                temp[i][idx] = temp[i][idx].split("\n")[0]
            if temp[i][idx] == "-": #하이픈을 0으로 바꾸는 작업
                temp[i][idx] = "0"

    year = input("연봉을 입력하세요(원 단위): ")
    year = str(int(year)/12)
    for searchidx, i in enumerate(temp):
        if temp[i][0] <= year < temp[i][1]:
            print(temp[i][0], ":월 급여액(천원단위)")
            print(searchidx)
            print(temp[searchidx])
            tax_free = input("비과세액을 입력하세요(원 단위): ")
            family = input("부양가족 수를 입력하세요(본인 포함): ")

            print("근로소득세:{}원".format(temp[searchidx][int(family)+1]))
            # public(year)
            # health(year)
            # convale(health)
            # employ(year)

def findError2(temp):
    temp2=[]
    for idx, i in enumerate(temp):
        templist = []
        for idx2, listitem in enumerate(temp[i]):
            if idx2 > 1:
                templist.append(listitem.isdigit())
        temp2.append(templist)
    print(temp2, "temp2")
    resultdict={}
    for idx2, i in enumerate(temp2):
        if temp2[idx2].count(True) != 11:
            if "notTrue" not in resultdict.keys():
                resultdict["notTrue"]=[]
            resultdict["notTrue"].append(idx2+1)
    return resultdict
errordict=findError2(temp)
print(errordict)

def checkRow(dict, rowIndex):
    print("\n")
    for idx, i in enumerate(dict):
        if idx == rowIndex:
            for j in dict[i]:
                if not j.isdigit():
                    print(j)

def checkNoise(dict, rowIndex):
    print("\n")
    for idx, i in enumerate(dict):
        if idx == rowIndex:
            for j in range(len(temp[rowIndex-1])):
                if j > 1:
                    for char in dict[i][j]:
                        if not char.isdigit():
                            dict[i][j]=dict[i][j].replace(char,"")
                    print(dict[i][j])

for i in errordict:
    for j in errordict[i]:
        checkRow(temp, j-1)
        checkNoise(temp, j-1)

a=["728", "720", "888", "666"]
def setAvrg(list):
    for i in range(len(list)):
        if not i == len(list)-1:
            if int(a[i])>int(a[i+1]):
                print(i, i+1, "정상")
            else:
                if int(list[i+2])!=0:
                    print(i,i+1,"비정상")
                    list[i+1]=int((int(list[i])+int(list[i+2]))/2)
setAvrg(a)
print(a)