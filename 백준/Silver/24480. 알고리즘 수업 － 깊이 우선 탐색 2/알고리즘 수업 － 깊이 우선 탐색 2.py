def dfs(cur_v):
    global cnt
    visited[cur_v] = cnt
    graph[cur_v].sort(reverse=True)
    for v in graph[cur_v]:
        if visited[v] == 0:
            cnt += 1
            dfs(v)

import sys
sys.setrecursionlimit(150000)
n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n+1)
cnt = 1

dfs(r)

for i in range(1, n+1):
    print(visited[i])