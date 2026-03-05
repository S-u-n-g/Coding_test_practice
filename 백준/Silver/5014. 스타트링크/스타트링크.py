import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())

visited = {}

def bfs(cur_v, target):
    visited[cur_v] = 0
    queue = deque()
    queue.append(cur_v)

    while queue:
        cur_v = queue.popleft()
        for next_v in (cur_v + u, cur_v - d):
            if next_v > f or next_v < 1:
                continue
            if next_v not in visited:
                visited[next_v] = visited[cur_v] + 1
                queue.append(next_v)
    
    if target in visited:
        print(visited[target])
    else:
        print("use the stairs")

bfs(s, g)