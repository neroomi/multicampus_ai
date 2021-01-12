from ai.file.fileProc import *

# 1번
# fileStream('hello.txt', 'asdf')

# 2번
# try:
#     fileStream('hello.txt', 'asdf')
# except Exception as e:
#     print('error -', e)
#
# print('end')


# 3번 - single line text inout
# fileStream('./ai/file/hello.txt', 'r')
# print('end')

# multi line text out
# withMultiWriter('multiline.txt')  # 임의적으로 디렉토리 경로 설정
# print('end')

lines = ['안녕하세요',
         '혹시 졸리우시면 ㅇㅇㅅㅋㄹ 콜?',
         '그럼 졸지말고 집중',
         '강사의 주옥같은 말을 한 귀로 흘리면 안돼요 ㅠ']

withListFileWriter('listline.txt', lines)

# multi line text read
withListFileRead('listline.txt', 'r')