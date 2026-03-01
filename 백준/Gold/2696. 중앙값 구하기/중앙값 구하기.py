import sys
from heapq import heappop, heappush

t = int(sys.stdin.readline())

for _ in range(t):
    left = []
    right = []

    n = int(sys.stdin.readline())
    print((n+1)//2)
    
    lines = ((n-1) // 10) + 1
    lst = []
    for _ in range(lines):
        lst += list(map(int, sys.stdin.readline().split()))
    cnt = 0

    for idx, x in enumerate(lst):
        i = idx + 1

        if len(left) == 0 or x <= -left[0]:
            heappush(left, -x)
        else:
            heappush(right, x)

        if len(left) > len(right) + 1:
            heappush(right, -heappop(left))
        elif len(left) < len(right):
            heappush(left, -heappop(right))            

        if i % 2 == 1:
            print(-left[0], end=" ")
            cnt += 1
            if cnt % 10 == 0:
                print()

    print()