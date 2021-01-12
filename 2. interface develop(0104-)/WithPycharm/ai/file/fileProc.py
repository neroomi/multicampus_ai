
'''
open(file = '파일경로/파일명', mode = 'r|w|a|wb')

# 파일생성 & 내용기록(ver.1) -> close 해줘야해
file = open(file='hello.txt', mode='w')
file.write('Hi, Sue')
file.close()

# 파일생성 & 내용기록(ver.2) -> close가 자동화된 구문(따로 안해줘도 됨)
with open() as file:
with open(file='hello.txt', mode='w') as file
    print(file.read())

# 파일읽기
file = open(file='hello.txt', mode='r')
print(file.read())
file.close()

'''

# # 1번
# def fileStream(fileName, mode):
#     if mode == 'w' :
#         pass
#     elif mode == 'r' :
#         with open(file=fileName, mode=mode) as file:
#             line = file.read()
#             print('result read -', line)
#     elif mode == 'a' :
#         pass
#     else :
#         raise Exception('모드를 확인하세요')


# 2번
# def fileStream(fileName, mode):
#     try :
#         if mode == 'w' :
#             pass
#         elif mode == 'r' :
#             with open(file=fileName, mode=mode) as file:
#                 line = file.read()
#                 print('result read -', line)
#         elif mode == 'a' :
#             pass
#         else :
#             raise Exception('모드를 확인하세요')
#     except Exception as e:
#         print('error - ', e)
#     finally:
#         if file != None:
#             file.close()


# 3번
# def fileStream(fileName, mode):
#     try :
#         if mode == 'w' :
#             pass
#         elif mode == 'r' :
#             with open(file=fileName, mode=mode) as file:
#                 line = file.read()
#                 print('result read -', line)
#         elif mode == 'a' :
#             file = open(file=fileName, mode=mode)
#             file.write('\nappend')
#         else :
#             raise Exception('모드를 확인하세요')
#     except Exception as e:
#         print('error - ', e)
#     finally:
#         if file != None:
#             file.close()

# 4번

def fileStream(fileName, mode):
    try :
        if mode == 'w' :
            file = open(file=fileName, mode=mode)
            file.write('sample text')
        elif mode == 'r' :
            with open(file=fileName, mode=mode) as file:
                line = file.read()
                print('result read -', line)
        elif mode == 'a' :
            file = open(file=fileName, mode=mode)
            file.write('\nappend')
        else :
            raise Exception('모드를 확인하세요')
    except Exception as e:
        print('error - ', e)
    finally:
        if file != None:
            file.close()


########## 멀티구문

def withMultiWriter(fileName):
    with open(fileName, 'w', encoding='utf-8') as file:
        for idx in range(3):
            print('idx - ', idx)
            text = input('문자열 입력 요망!! >>> ')
            file.write('{} - {}\n'.format(idx, text))

def withListFileWriter(fileName, dataset):
    with open(fileName, 'w', encoding='utf-8') as file:
        for idx in range(len(dataset)):
            print('idx - ', idx)
            file.write('{} - {}\n'.format(idx, dataset[idx]))

def withListFileRead(fileName, mode):
    with open(fileName, mode, encoding='utf-8') as file:
        line = None
        # while line != '':                 # 방법 1
        #     line = file.readline()
        #     print(line.strip('\n'))

        # for line in file.readlines():       # 방법 2
        #     print(line.strip('\n'))

        # for line in file:                   # 방법 3
        #     print(line.strip('\n'))