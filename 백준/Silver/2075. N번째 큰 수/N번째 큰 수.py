import sys
from heapq import heappop, heappush

n = int(sys.stdin.readline())

pq = []

for _ in range(n):
    lst = list(map(int, sys.stdin.readline().split()))
    for x in lst:
        heappush(pq, x)
        if len(pq) > n:
            heappop(pq)

print(pq[0])