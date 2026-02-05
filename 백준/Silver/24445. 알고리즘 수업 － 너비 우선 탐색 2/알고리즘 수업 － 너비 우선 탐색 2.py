import sys
from collections import deque

def bfs(cur_v):
    global cnt
    queue = deque()
    visited[cur_v] = cnt
    queue.append(cur_v)

    while queue:
        next_v = queue.popleft()
        graph[next_v].sort(reverse=True)
        for v in graph[next_v]:
            if visited[v] == 0:
                queue.append(v)
                cnt += 1
                visited[v] = cnt

n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n+1)
cnt = 1

bfs(r)

for i in range(1, n+1):
    print(visited[i])