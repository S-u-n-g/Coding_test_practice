import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

dic = {}

for i in a:
    dic[i] = True

for i in b:
    if i in dic:
        print(1)
    else:
        print(0)