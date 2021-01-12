

'''
*** 학습목표 ***
다중상속 : 부모를 한 명 이상 갖겠다
추상화
데코레이션
제너레이터
이터레이터

'''

class Animal(object):
    def cry(self):
        pass
class Tiger(Animal):
    def jump(self):
        print('호랑이가 점프를 한다')
    def cry(self):
        print('어흥')
class Lion(Animal):
    def bite(self):
        print('한 입에 꿀꺽한다')
    def cry(self):
        print('그르렁')
class Liger(Tiger, Lion):    # 순서에 따라 먼저 정의되는 함수 내용을 따라갈 수 있음
    def play(self):
        print('라이거가 사육사와 재미있게 놀고 있다')


# 추상 클래스

'''
- 클래스를 만드는 이유 -> 객체생성
- 추상클래스 객체생성 X
- 추상메서드(함수)를 하나라도 가지면 추상클래스
- 함수 구현을 강제하기 위해서 사용
'''

from abc import *

class Base(metaclass=ABCMeta):
    @abstractmethod     # 추상메서드로 만들기
    def study(self):
        pass
    def goToSchool(self):
        print('hard study')

class Student(Base):
    def study(self):
        print('공부하자~')


# 특수문법  -  데코레이션
'''
Decorator은 함수의 인자로 다른 함수를 전달하는 과정에서 적용할 수 있는 문법
'''

def outerFunc(func):    # 이건 외부함수
    def innerFunc():    # 내장함수 ( 중첩됨 )
        func()
    return innerFunc()

def userFunc():
    print('userFunc 함수가 수행되었습니다')

myFunc = userFunc()
myFunc


# userFunc()

decoratorFunc = outerFunc(userFunc)
decoratorFunc




import time
def userOuterFunc(func):
    def userInnerFunc():
        print('{} 함수수행 시간을 계산합니다.'.format(func.__name__))
        start = time.time()
        func()
        end = time.time() - start
        print('{} 함수수행 시간은 {}입니다.'.format(func.__name__, end))
    return userInnerFunc()

decoratorUserFunc = userOuterFunc(userFunc)
decoratorUserFunc


#####################


import datetime
def loggerLogin():
    print(datetime.datetime.now())
    print("sue's login")
    print(datetime.datetime.now())

loggerLogin()


############


def loggerLoginSue():
    #print(datetime.datetime.now())
    print("sue's login")
    #print(datetime.datetime.now())


def loggerLoginKing():
    #print(datetime.datetime.now())
    print("king's login")
    #print(datetime.datetime.now())

def datetimeDecorator(func) :
    def wrapper():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return wrapper

sue = datetimeDecorator(loggerLoginSue)
sue()
king = datetimeDecorator(loggerLoginKing)
king()



############

@datetimeDecorator
def dumpFunc():
    print('함수 실행~')
dumpFunc()



#############

'''
1. typeChecker Decorator 만들기(인자의 유효성 검사)
- digit01, digit02를 곱한 값을 출력하는 함수
- typeChecker Decorator로 digit01, digit02가 정수가 아니면
- 'only integer support' 출력
'''

def typeChecker(func):
    def innerFunc(digit01, digit02):
        # 유효성검사
        if type(digit01) != int or type(digit02) != int:
            print('only integer support')
            return      # 실행을 종료하겠다(함수 자체가 종료)
        return func(digit01, digit02)
    return innerFunc

# 사용
@typeChecker
def div(digit01, digit02):
    return digit01 * digit02

msg = div(3, 1)
print(msg)
div(0.1, 1)



######################

# 파라미터와 관계없이 모든 함수에 적용 가능한 Decorator 만들고 싶다면?
# *args, **args

def generalDeco(func):
    def wrapper(*args, **kwargs):
        print('this is decorated')
        return func(*args, **kwargs)
    return wrapper

@generalDeco
def userSquare(digit):
    return digit *digit
print(userSquare(2))

@generalDeco
def userPlus(digit01, digit02):
    return digit01 + digit02
print(userPlus(2, 3))

@generalDeco
def userPlus(digit01, digit02, digit03, digit04):
    return digit01 * digit02 * digit03 * digit04
print(userPlus(2, 3, 4, 5))


################

def makeBold(func):
    def wrapper(string):
        return '<b>' + func(string) + '</b>'
    return wrapper

def makeFont(func):
    def wrapper(string):
        return '<i>' + func(string) + '</i>'
    return wrapper

@makeBold
@makeFont
def makeBoldFont(string):
    return string

print(makeBoldFont('두 개의 데코레이터 활용중'))


# class - function 데코레이터 적용이 가능할까?
# YES!

def tagH1(func):
    def wrapper(self, *args, **kwargs):
        return '<h1>{}</h1>'.format(func(self, *args, **kwargs))
    return wrapper

class Per(object):
    def __init__(self, name):
        self.name = name
    @tagH1
    def getName(self):
        return self.name

per = Per('sue')
print('per - ', per.getName())


################

# Iterator
'''
- 순환 반복
- 실행 속도가 빨라져

# iterable 객체(iterable Object)
:list, set, tuple, dict - (collection)
:text sequence
:for ~ in collection:
    pass
    
# iterator 
-> 파이썬이 기본적으로 가지고 있는 내장함수(iterable과 혼동하지 말 것!)
-> 순차적으로 다음 데이터를 리턴할 수 있는 객체
-> 내장함수 next() 사용해서, 순환하는 다음 값을 반환함
-> 대용량에서는 iterator를 쓰는 게 더 좋음
'''
for num in [1, 2, 3, 4, 5]:
    print(num)

for char in 'text sequence':
    print(char)

 userList = [1, 2, 3, 4, 5]        # iterator가 아니라 iterable이라서
# print(next(userList))             # next 함수를 사용할 수 없다 -> 당근 오류남

userIterator = iter(userList)
print('type - ', userIterator, (userIterator), type(userList))
print(next(userIterator))


# 사용자 정의 iterator 클래스 만들어보자
class Counter:
    def __init__(self, stop):
        self.stop = stop
    def __iter__(self):
        return CounterIterator(self.stop)

class CounterIterator:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop
    def __next__(self):
        if self.current < self.stop:
            rtnValue = self.current
            self.current += 1
            return rtnValue
        else:
            pass

cntIterator = iter(Counter(10))
print(next(cntIterator))

############

# Comprehension
'''
[출력표현식 for 요소 in sequence [if 조건식]]  - list
{출력표현식 for 요소 in sequence [if 조건식]}  - set / python 3.0 이상만
{key:value for 요소 in sequence [if 조건식]}  - dictionary / python 3.0 이상만
'''
dataset = [4, True, 'sue', 3.1, 10]
# 위 데이터 셋에서 정수값만 출력을 원한다면?
inType = [value ** 2 for value in dataset if type(value) == int]
print('int type - ', type(inType), inType)

dataset = [1, 1, 2, 2, 3, 3, 4, 4]                  # set은 중복이 없음
setType = {value * value for value in dataset}      # set은 순서가 없음
print('set type - ', type(setType), setType)
# 결과값 {16, 1, 4, 9} -> 순서 의미 없음

dataset = {1: 'sue',  2: 'jung', 3: 'kyung'}
print('dict keys -', dataset.keys())
print('dict values -', dataset.values())
print('dict dict items -', dataset.items())

# key 값이 1 이상인 데이터를 값:키 형식으로 새로운 set 만든다면?

keySet = {value:key for key, value in dataset.items() if key >= 1}
print('dict comprehension - ', type(keySet), keySet)
# 나의 try
# dictType = print('{}:{}'.format(dataset.values(), dataset.keys())) if dataset.values() >= 1
# print('dict type -', dictType)


# key값을 10단위로 한번에 바꿔본다면?
keySet = {key*10:value for key, value in dataset.items()}
print('dict comprehension -', type(keySet), keySet)


#############

# python generator
'''
iterator를 만들어주는 기능
yield 키워드 이해
'''

def textSequenceFunc():
    msg = 'hi python'
    for txt in msg:
        yield txt          # 함수가 더이상 돌지 않고 끝이 나서 결과값 'h'만 출력
# print(textSequenceFunc)
textSequenceFunc()

charIte = iter(textSequenceFunc())
print(type(charIte))
print(next(charIte))


## python generator
'''
iterator를 쉽게 해주는 기능
yield 키워드 이해
메모리 성능 때문에 loop를 컨트롤하기 위해 쓰여지는 루틴
'''
'''
## yield
- 잠시 함수 실행을 멈추고 호출한 곳에 값을 전달
- 현재 실행된 상태를 계속 유지
- 그러므로, 다시 해당 함수를 호출하면 현재 실행된 상태를 기반으로 다음 코드를 실행
'''
print(textSequenceFunc())
charIte = iter(textSequenceFunc())
next(charIte)

def userGeneratorFunc(data):
    # result = []
    for tmp in data:
        # result.append(tmp * 2)
    # return result
        yield tmp * 2


twiceList = userGeneratorFunc([1, 2, 3, 4, 5])
print('처리된 결과 - {}'. format(twiceList))
print(type(twiceList))
# print('next - {}'.format(next(twiceList)))
for t in twiceList:
    print(t)


###################

# Generator Comprehension()
# (Lazy Operation)
'''
syntax)
(출력형식 for 요소 in collection)
'''
squareData = (num ** 2 for num in range(5))
print(type(squareData))
# print(sum (squareData))
for data in squareData:
    print(data, end='\t')