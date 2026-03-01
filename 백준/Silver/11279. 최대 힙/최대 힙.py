import sys
from heapq import heapify, heappop, heappush

n = int(sys.stdin.readline())

pq = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(pq) == 0:
            print(0)
        else:
            print(-heappop(pq))
    else:
        heappush(pq, -x)
