# Git Command

> Git 명령어 정리





## 초기설정



### 0. init

- `git init`

- `.git/` 폴더를 생성해준다.

<img src="Git Command.assets/image-20201229151435595.png" alt="image-20201229151435595" style="zoom:150%;" />

- `.git` 폴더가 생성된 경우 오른쪽에 `master` 라는 표시가 나온다.
- 최초에 한 번만 하면 된다.



### 1. config

- `git config --global user.email "myemail@gmail.com"`

  - 이메일의 경우 깃헙에 올릴 때 잔디 심는 기준이므로 정확히 입력

- `git config --global user.name "myname"`

- 최초에 한 번만 하면 된다. (바꾸려면 주소만 바꿔서 다시 입력)





## 커밋기록



### 1. add

- `git add <추가하고 싶은 파일>`
  - `git add . ` : 현재 폴더의 모든 파일과 폴더를 add(띄어쓰기에 주의)
- working diretory => staging area로 파일 이동



### 3. commit

- `git commit -m "message"`
- 스냅샷을 찍는 동작
- add 되어있는 파일들을 하나의 묶음으로 저장
- 메세지에 들어가는 내용은 기능 단위로 할 것
- 한 번만 해도 됨
- 만약 git commit 다음에 -m 을 통해 메세지를 안 적으면 이상한 화면에 갇힘
  - INSERT 눌러 첫째줄에 메세지 입력 -> esc 통해 최하단 줄에 :wq 입력 후 Enter -> 탈출



### 4. remote

- `git remote add origin <address>`
- 원격 저장소와 현재 로컬 저장소를 연결



### 5. push

- `git push origin master`
- 깃아 올려줘 origin으로 master을
- 원격저장소에 로컬 저장소의 데이터를 전송





## 상태확인



### 1. status

- `git status`
- 현재 git 상태를 출력



### 2. log

- `git log`

- 커밋 기록을 전체 다 출력
- 옵션
  -  `--oneline` : author, date 같은 정보를 제외하고 한 줄로 출력
  - `--graph` : 커밋들을 점으로 표현하고 그 커밋들을 선으로 연결하여 그래프 형태로 출력



### 3. diff

- `git diff`
- 현재 변경사항을 체크 (add 하기 전에)





## 추가파일



### 1. gitignore

- `.gitignore` 파일을 생성 후 git으로 관리하고 싶지 않은 파일들을 저장
- ```gitignore.io```







## 기타



### clone

- 전체 파일을 다운로드



### pull

- 바뀐 부분만 다운로드







## 브랜치



### 1. 생성

- `git branch <브랜치 이름>`



### 2. 이동

- `git switch <브랜치 이름>` => 최신문법
- `git checkout <브랜치 이름>` => 좀 더 예전 문법



### 3. 삭제

- `git branch -d <브랜치 이름>`



###  4. 병합

- `git merge <브랜치 이름>` 

- base가 되는 branch로 이동해서 명령어 사용
- 충돌이 발생하 경우 => 충돌 해결(>>없애거나 둘 중 하나 택하거나 등) 후, 다시 add, commit, push