
print('a','b', end='')
print('c')
youNme = 1
you    = 2
number = 3
print(youNme)
print(you)
print(number

a = 9.46e12
print(a)

a = 1 +2j
b = 3 + 4j
print(a + b)


print("I\thave\tan\napple")
print(365*24*60*60)

s = ("k" 
    "j" 
    "2002")
print(s)

for c in range(ord('A'), ord('Z')+1):
    print(chr(c), end= '')


a = 'He said "Great!"'
b = "Let's go!"
c = 'I Say "Help" to you'
d = 'don\'t go'

print(a, b, c, d)


r = range(1, 10, 2)
print([r])


#### HELP / 검토하기
def calcrange(begin, end, step):
    sum = 0
    for num in range(begin, end + 1, step):
        sum += sum
    return sum
print("3~30", calcrange(3, 30, 2))