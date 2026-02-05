import sys
from collections import deque

def bfs(cur_v):
    queue = deque()
    visited.append(cur_v)
    queue.append(cur_v)

    while queue:
        next_v = queue.popleft()
        graph[next_v].sort()
        for v in graph[next_v]:
            if v not in visited:
                queue.append(v)
                visited.append(v)

def dfs(cur_v):
    visited.append(cur_v)
    graph[cur_v].sort()
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)

sys.setrecursionlimit(150000)
n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = []
dfs(r)

for v in visited:
    print(v, end=" ")
print("")

visited = []
bfs(r)

for v in visited:
    print(v, end=" ")