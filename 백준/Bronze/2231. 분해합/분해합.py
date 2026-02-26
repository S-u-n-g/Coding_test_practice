import sys

num = int(sys.stdin.readline())

start = max(0, num - (9 * len(str(num))))
succ = False

for i in range(start, num):
    result = i
    for j in str(i):
       result += int(j)
    if result == num:
        print(i)
        succ = True
        break

if not succ:
    print(0)