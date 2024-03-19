#240118 클래스

#객체 지향 프로그래밍 언어
#객체 개체 object : OOP
#객체를 우선으로 생각해서 프로그래밍을 한다
#클래스 기반의 프로그래밍 언어
#클래스를 기반으로 객체를 생성한다.

#필요한 요소만을 사용해서 객체를 표현하는 것 : 추상화
#속성을 가질 수 있는 것 : 객체


#클래스 선언 : 틀을 정의
# class classname:
#     def __init__(self): #생성자 함수의 정의 __init__(self)
#         pass
#
# #클래스 내부 함수는 첫 매개변수로 self 입력
# #self : 자기 자신
#
# #클래스는 클래스 이름과 같은 함수(생성자)를 통해 객체를 만들어 낸다.
# classname1 = classname() #classname클래스를 틀로 사용해서 classname1객체 만듬
#
# class Student:
#     num = 1
#     def __init__(self, name): #생성자
#         self.name=name #self는 자기자신 #name 변수를 만든 것 #뒤에 name은 매개변수
#         self.age = 100
#         print("생성자")  # -> 클래스명을 가지고 호출할 때 출력됨/프로그램이 실행될 때 호출
#     def __del__(self):
#         print("소멸자") #프로그램이 종료될 때 호출
#     def xxx(self):
#         self.name = "111"
#
# x = Student("3번학생")
# x2 = Student("4번학생")
# print(type(x))
# print(x.num)
# print(x.age)
# print(x.name)
# print(Student.num)
# #print(Student.age) --> 에러
# x.xxx()


#학생을 생성할 수 있는 클래스 구조를 만든다.
#모든 학생은 1번강의실에 소속되어 있다. #공통사항 => 변수
#개인별 학생은 이름, 나이, 국어, 영어, 수학 #개별사항 => self 변수
#학생을 객체로 3명 만들어서
#학생 중 성적의 평균이 가장 높은 학생의 [소속 강의실 번호, 이름, 나이]를 출력

class Student:
    classroom = "classroom_1"
    def __init__(self, name, age, kor, eng, math):
        self.name = name
        self.age = age
        self.kor = kor
        self.eng = eng
        self.math = math
        self.avg = 0

    def cal_avg(self):
        self.avg = (self.kor + self.eng + self.math) / 3
        return (self.kor + self.eng + self.math) / 3

students = [
        Student("윤하얀", 24, 95, 88, 83),
        Student("배송원", 24, 90, 87, 78),
        Student("박가영", 23, 93, 92, 80),
    ]

for i in students:
    i.cal_avg()

max = [0,0]
for idx, i in enumerate(students):
    if i.avg > max[0]:
        max[0] = i.avg
        max[1] = i.name

print(Student.classroom, max[1])