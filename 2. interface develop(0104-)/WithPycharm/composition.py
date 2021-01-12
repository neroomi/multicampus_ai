

'''
학습목표
Composition == Aggregation
상속을 피하고 클래스의 일부 기능을 그대로 활용하고 싶을 때
'''

class Calc01(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def multiply(self):
        return self.x * self.y

class Calc02(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def multiply(self):
        return self.x * self.y


class UserCalc:     # 완전 상속은 아니과 필요부분만 사용하고파
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cal02 = Calc02(x, y)    # 객체를 명시적으로 생성
    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y
    def multiply(self):
        return self.cal02.multiply()

calc = UserCalc(3, 4)
print('calc multiply -', calc.multiply())


###################

'''
- 예외(Exception) - SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError ......
- 처리할 수 있는 구문
try :
    에러가 발생할 가능성이 있는 코드
    정상코드
    에러가 발생할 가능성이 있는 코드
    정상코드
except xxxxError :
    1. 프로그램의 흐름을 정상으로 컨트롤
    2. 예외발생의 디버깅
    3. 로그파일 만들어서 예외정보를 저장
except xxxxError :
    발생된 에러를 잡기 위한 객체 정의
else :
    에러가 발생되지 않을 때 실행되는 블럭
finally :
    무조건 수행
'''

#### 에러 확인하기
# print('error)
# a = 10
# b = 20
# print(c)
# print(100/0)
# print('*' * 50)
# print('end')



# def userKeyIn():
#     try:
#         age = int(input('본인의 나이 입력하세요 :'))
#         print('예외 발생 이후 code')
#     except ValueError as e :
#         print('error =', e)
#     print('함수 실행 종료')
# userKeyIn()


def userKeyIn():
    try:
        age = int(input('본인의 나이 입력하세요 :'))
        print('예외 발생 이후 code')
    except Exception as e :     # 다중 except error를 쓰기 싫을 때 사용
        # print('error =', e)     # 디버깅(개발자에게 알리는 것)
        print('문자열이 아닌 정수를 입력해 주세요~')
        userKeyIn()
    else:
        print('age - ', age)
        print('함수 실행 종료')
    finally:       # 예외 정의 상관 없이 항상 실행되는 영역
        print('넌 너무 지조가 없다....항상 실행되니까!!!')
userKeyIn()



########## 내가 시도
# nameList = ['kim', 'lee', 'park', 'jung']
# name = 'cho'
# idx = nameList.index(name)
# print('{} Found it !! {}'.format(name, idx+1))
# print('{} Not Found it !! {}'.format(name, idx+1))
# try:
#     name = input('이름을 입력하세요:')
# except:
#     print('{} Not Found it !! {}'.format(name, idx+1))
#     print('다시 입력해주세요')
# else:
#     print('{} Found it !! {}'.format(name, idx+1))

# name = input('이름을 입력하세요:')

########## 해결방법
nameList = ['kim', 'lee', 'park', 'jung']
try:
    name = 'lee'
    idx = nameList.index(name)
except ValueError as e:
    print('{} Not Found it !! {}'.format(name, idx+1))
else:
    print('{} Found it !! {}'.format(name, idx+1))
finally:
    print('예외 여부와 상관없이 항상 실행되는 블럭')
print('프로그램 종료')


###############

# 클래스에 정의된 함수에 예외처리 적용 및 강제 예외 발생

# 예외발생전
# class Account:
#     def __init__(self, account, balance, interestRate):
#         self.account = account
#         self.balance = balance
#         self.interestRate = interestRate
#     def withDraw(self, amount):
#         if self.balance < amount:   # 이 부분이 예외
#             raise Exception
#         else:
#             self.balance -= amount


#######
# 사용자 정의 예외 클래스를 작성
class InsufficientError(Exception):
    def __init__(self, msg):
        self.msg = msg



# 예외처리중
class Account:
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
    def withDraw(self, amount):
        try:
            if self.balance < amount:   # 이 부분이 예외
                raise InsufficientError('잔액이 부족합니다~')
        except Exception as e:
            print('error msg - ', str(e))
        else:
            self.balance -= amount

    def withDraw02(self, amount):
        if self.balance < amount:   # 이 부분이 예외
            raise InsufficientError('잔액이 부족합니다~')
        else:
            self.balance -= amount

account = Account('100', 100000, 0.073)
try:
    account.withDraw02(20000)
except InsufficientError as e:
    print(str(e))
account.withDraw(200000)
print('프로그램 종료')


'''
객체생성 - 클래스(변수,함수)
클래스없이 객체를 생성하는 방법(변수)
class A:
    def __init__ sese
usage).......
collections.namedtupe((변수) [변수])
'''

import collections
# Person = collections.namedtuple('Person', ['name id'])
# Person = collections.namedtuple('Person', 'name, id')
Emp = collections.namedtuple('Person', 'name, id')
per = Emp('sue', '100')
print(per, type(per))


# 속성에 접근
print('idx 0 -', per[0])
print('idx 1 -', per[1])

for idx in range(len(per)):
    print('idx {} - {}'.format(idx, per[idx]))

# 속성에 접근 2
print(per.name)
print(per.id)

# 속성에 접근 3
name, id = per
print(name, id)


###############

# 미션 도전!
'''
1. 직장인 이름, 나이, 부서를 속성으로 갖는 클래스 만들기
2. 직장인 이름, 나이, 부서를 속성으로 갖는 클래스를 namedtuple로 만들기
'''

class Mission:
    def __init__(self, name, age, dep):
        self.name = name
        self.age  = age
        self.dep  = dep

Emp = collections.namedtuple('mp', ['name', 'age', 'dept'])
emp = Emp('sue', 20, 'cs')
print(emp01.name, mission01.age, emp 01.dept)