
# from ai.oop import oop_inheritance import Car
from ai.oop.oop_inheritance import *


# car01 = Car('GV70', 4, 2400)
# car01.carInfo()

# parent = Parent('부모', '공무원')
# print('parent - ', parent)
# print('parent -', parent.display())
#
# child01 = Child01('자식', '강사', 49)
# print(child01.display())
#
# stu01 = StudentVO('수경', '20', 'seoul', '2021')
# print("stu info -", stu01.stuInfo())
#
# tea01 = TeacherVO('경수', '20', 'seoul', 'python')
# print('tea info - ', tea01.teaInfo())
#
# emp01 = ManagerVO('장호연', 29, 'seoul', 'HRD')
# print('emp info - ', emp01.empInfo())


# 1번
# userDate = MyDate(2021)   # -2021로 써도 출력가능
# print(userDate.year())    # 정보의 보안성이 떨어진다


# 3번 -> (__했을시에 오류가 남 = 변수에 대한 직접적 접근 막아주는 것)
# userDate = MyDate()
# userDate.year = -2021
# print(userDate.getYear())


# 4
userDate = MyDate()
userDate.setYear(-2021)
print(userDate.getYear())



# # 5 은닉화 공부
# hiding = HidingClass('홍길동', '교육팀', 100)
# print('utype - ', hiding.utype)
# print('name - ', hiding.name)
# # print('dept - ', hiding.__dept)
# print('num - ', hiding.num)
# print('call getDept -', hiding.getDept())
# print('call __getInfo -', hiding.__getInfo())


# Account Caller
account = Account('44102919-1234', 500000, 0.073)
account.accountInfo()
account.withDraw(600000)
account.deposit(200000)
account.accountInfo()
account.withDraw(600000)
account.accountInfo()
print('현재 잔액의 이자를 포함한 금액')
account.printInterestRate()
