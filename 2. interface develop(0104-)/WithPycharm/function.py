
# python function

'''
함수는 가독성을 높이기 위한 방법으로
하나 이상의 본문을 가지는 코드는 함수로 정의하는 것이 좋다
내장함수 | 사용자정의 함수
함수를 정의할 때는 def 키워드를 이용해서 함수를 정의
'''


# user define function
'''
def return_type function_name(argument)
def function_name() <- 여러개 들어갈 수 있음

def function_name():
    statement
    return value(built-in type)
'''
def user_print():
    print('user_print')

# from digital.python import package_function
# package_function.print_coins()

# from digital.python import package_function as f
#f.print_coins()

#from digital.python.package_function import print_Coins
#print_Coins()

from digital.python import package_function as f

#r_message = f.returnfunc()
#print('call returnfunc() - ', r_message)

e_mesage = f.say_echo('잇룡')
print('call say_echo()-', e_mesage)

domain = f.make_url('naver')
print('call make_url() - ', domain)

f.bad_func('메롱')

tup_rtn = f.tuple_func(1, 2, 3, 4, 5, 6 , 7, 8, 9)
print('call tuple_func() - ', tup_rtn)


f.dict_func(name='sue', age='top secret')

(odd_sum, even_sum) = f.cnt_sum(100, 500)
print('홀수의 합 {}, 짝수의 합 {}'.format(odd_sum, even_sum))


# 인자로 넘겨받은 연도 사이의 윤년을 찾아 리턴시켜주는 함수를 작성한다면?
# list 타입
leapyear_list = f.leapyear_func(1990, 2021)
print('leapyear_list -', type(leapyear_list), leapyear_list)

dict_msg = f.rtn_dict_func(10)
print('dict_msg -', type(dict_msg), dict_msg)



# defaut parameter 사용

def default_param(x, y, z = True):
    param_sum = x +y
    if param_sum > 0 and z:
        return param_sum
    else:
        return 0

# caller function
result = default_param(10, 20, False)
print('caller default_param() - ', result)


# 함수의 입력인자가 list, dict - mutable(수정가능)
# 함수의 입력인자가 숫자, 문자열, tuple - immutable(수정불가능)
tmp_list = [10]
tmp_x = 10
def mutable_func(arg_x, arg_list):
    arg_x = arg_x + 100
    arg_list.append(100)


mutable_func(tmp_x, tmp_list)
print('tmp_list : ', tmp_list)
print('tmp_x : ', tmp_x)

# varialbe(변수) - 선언 위치에 따라서(local, global)

tmp = 100

def my_func(x):
    tmp = 0
    tmp += x
    return tmp

print('caller my_func : ', my_func(100))




# 새로운 함수
def person_info(weight, height, **other):
    print('weight : ', weight)
    print('height : ', height)
    print('extra : ', other, type(other))  # dict


person_info(50, 177, name = 'sue', address = 'seoul')


# 새로운 함수
def overroll(args01, args02, *args03, **args04):
    print(args01, args02, args03, args04)

overroll(10, 20, 'lee', 'kim', 'park', 'cho', age01=20, age02=30, age03=40)


# nested function(중첩함수)
def outer_func(outer_num):
    def inner_func(num):
        print('inner_func - ', num)
    inner_func(outer_num + 100)

outer_func(100)
# inner_func(100) - 실행불가 즉, 호출 불가합니다


'''
중첩함수 활용 예)
outer 함수 : 자료(data) 생성, inner 함수 포함
inner 함수 : 자료 연산/처리(합계, 평균)
'''

# 그냥
def cal_func(data):
    pass

data = list(range(1, 101))
print('range data - ', data)



# 중첩
def cal_func(data):
    dataset = data
    def sum_func():
        total = sum(dataset)
        return total
    def avg_func(total):
        avg = total / len(dataset)
        return avg
    return sum_func, avg_func


data = list(range(1, 101))
print('range data - ', data)


rtn_sum_func, rtn_avg_func = cal_func(data)
tot = rtn_sum_func()
print('tot - ', tot)
avg = rtn_avg_func(tot)
print('avg - ', avg)


'''
재귀함수(self-recursive function)
- 함수 내부에서 자신의 함수를 반복 호출하는 기법
- 용도 : 반복적으로 변수를 변경해서 연산할 때(누적, 팩토리얼)
'''

def count_func(n): # n = 5 -> 1, 2, 3, 4, 5
    if n == 0:
        return 0
    else:
        count_func(n-1)  # stack [5, 4, 3, 2, 1]
        print(n, end=" ")

count_func(5) # 1 2 3 4 5
count_func(0) # 0


# 누적 : (n) = 1 + 2 + 3 + ...... + n
def add_sum(n):
    if n == 1:
        return 1
    else:
        result = n + add_sum(n-1)
        print('debug - ', result)
        return result

print('n=5 :', add_sum(5))  # 왜 역순으로 호출되는가 stack에 쌓고 나서 역순 호출?
print('n=100 :', add_sum(100))



# 익명의 함수(lambda 식)을 만드는 방법 -> BUT 비교적 간단할 때 사용해라
# lambda식( 가독성 향상, 코드 간결, 메모리 절약 - 즉시 실행 함수라서)

def multi_func(x, y):
    return x * y
print(multi_func(10, 50))

# syntax : lambda arg : body

lambda_var = lambda x, y : x * y
print(lambda_var(10, 50))



#
def lambda_func(x, y, func):
    print('lambda_func - ', x * y *func(100, 100))

lambda_func(10, 20, lambda x, y : x * y)
lambda_func(10, 20, lambda_var)
lambda_func(10, 20, multi_func)


# hint
def tot_length_func(word : str, num : int):
    return len(word) * num

print('hint -', tot_length_func("baaaam", 10))