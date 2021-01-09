

# python 객체지향 프로그래밍 (oop)

'''
패키지(package) > 모듈(module) > 클래스(class) > 함수(function)
Object Oriented Programming(OOP)

Real World             추상화                 P/G(프로그램 영역)
Object -------------   Class   ----------->  Instance
- 명사적 특징    -----   변수
- 동사적 특징    -----   함수
'''


# 학생의 정보를 저장하려고 합니다
stuName = '수경'
stuMajor = '컴공'
stuId = '2020'
stuGrade = 4.5

# 추천하지 않는다
stuNameList = ['수경', '경수']


# class를 이용해서 한 학생의 데이터를 논리적인 하나의 단위로 묶어서 사용


'''
     class  vs  instance
namespace         : 객체를 인스턴승화할 때 저장된 공간
class variable    : 직접 접근가능 및 공유
instance variable : 객체 소유로 별도 존재 

class
- 함수의 모임
- 역할 : 여러 개의 함수와 공유데이터를 묶어서 객체 생성할 수 있는 템플릿
- 구성 : 멤버 = 변수(데이터) + 메서드(함수), 생성자(초기화)
- 형식 :      class 클래스이름 : 
                   변수              - 자료 저장
                   초기화            - 객체 생성시 호출되는 함수
                   def 함수이름() :   - 자료처리 

self - instance의 소유라는 걸 명시한다

'''

class Calc:
    x = 0
    y = 0

    def __init__(self):
        print('객체 생성시 호출되는 함수, 초기화')
    def plus(self):
        print('사용자 정의 함수, 인스턴스의 소유가 됨')


# instance 생성하는 문법
obj = Calc()      # 인스턴스: 클래스가 메모리에 생성된 상태
                  # 정확히는 아니지만 이해를 위해 일단 '클래스로부터 생성된 객체'라고 생각하자
                  # 그럼 인스턴스 생성 = 객체 생성 -> init 함수 생성 -> print 내용 출력
obj.plus()


# instance 생성하는 문법

'''
user define function
- setXXXX
- getXXXX
- is XXXX
'''

class Student:

    def __init__(self, name, major, num, grade):
        self.name  = name
        self.major = major
        self.num   = num
        self.grade = grade

    def __repr__(self):
        return self.name +"\t"+ self.major +"\t"+ self.num +"\t"+ str(self.grade)

    def getInfo(self):
        return '이름 : {} \t 전공 : {}'.format(self.name, self.major)



stu01 = Student('수경', '컴공', '2020', 4.5)
print('stu01 address -', stu01)
print(stu01.name)
print(stu01.major)
print(stu01.num)
print(stu01.grade)


stuList = []
stu01 = Student('수경', '철학', 1992, 4.5)
stu02 = Student('경수', '컴공', 1992, 4.5)
stu03 = Student('정수', '경영', 1992, 4.5)

stuList.append(stu01)
stuList.append(stu02)
stuList.append(stu03)
for stu in stuList:
    print(stu.getInfo())

print(id(stu01), id(stu02), id(stu03))


stuList.append(Student('수경', '철학', 1992, 4.5))
stuList.append(Student('경수', '컴공', 1992, 4.5))
stuList.append(Student('정수', '경영', 1992, 4.5))
for stu in stuList:
    print(stu)


# 인스턴스 소유의 변수가 아닌 클래스 소유의 변수 ( 조금 더 어려운 거 ! )
# namespace (instance -> class -> super class)

class Student:
    scholarshipRate = 3.5 # class variable(클래스 소유O, 인스턴스 소유가 아님)
    def __init__(self, name, major, num, grade):
        self.name  = name
        self.major = major
        self.num   = num
        self.grade = grade

    def __repr__(self):
        return self.name +"\t"+ self.major +"\t"+ self.num +"\t"+ str(self.grade)

    def getInfo(self):
        return '이름 : {} \t 전공 : {}'.format(self.name, self.major)

    def isScholarship(self):
        if self.grade >= Student.scholarshipRate: #(인스턴스 소유가 아니므로 클래스로 접근해야해)
            return True
        else:
            return False

stu01 = Student('이중현', '기계공학', '2010', 4.0)
print('장학금 여부 - ', stu01.isScholarship(), Student.scholarshipRate)


# 인스턴스 소유가 아닌   class method

'''
self X
클래스 함수는 cls인 인자를 받고 모든 인스턴스가 공유하는 클래스 변수와
같은 데이터를 생성, 변경 또는 참조하기 위해 사용
'''

class Employee:

    raiseRate = 1.1   # 급여인상률 class variable(class 소유의 함수)

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary
    def getSalary(self):
        return '현재 {}님의 급여는 {}입니다'.format(self.name, self.salary)

    @classmethod    # cls시 꼭 해줘야 함!
    def updateRate(cls, rate):  # class 소유 변수라서 self 대신 cls
        print('인상률이 {}에서 {}로 변경되었습니다'.format(Employee.raiseRate, rate))
        cls.raiseRate = rate

    def applyRaise(self):
        self.salary = int(self.salary * Employee.raiseRate)  # Employee.raiseRate 대신 cls.raiseRate는 불가

    # static 함수 (cls나 self를 갖지 않는 함수)
    @staticmethod  # 꼭 사용해줘야 함!
    def isValid(salary):
        if salary < 0 :
            print('음수가 될 수 없습니다')


emp01 = Employee('회사원1', 1000)     # 인스턴스 생성
print('인상 전 급여 -', emp01.getSalary())

Employee.updateRate(1.5)    # self가 없으므로 class 소유의 함수
emp01.applyRaise()

print('인상 후 급여 -', emp01.getSalary())

Employee.isValid(-1)  # 모르겠으면 무시 !
