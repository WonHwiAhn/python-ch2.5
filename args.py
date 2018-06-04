# commnad line의 arguments 처리

import sys

# sh에서 #python args.py Hello World 이런식으로 명령어를 입력했을 경우에 args가 들어감

print(sys.argv)

args = sys.argv[1:]
print(args)