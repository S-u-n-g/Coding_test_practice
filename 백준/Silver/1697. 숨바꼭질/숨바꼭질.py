import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

visited = {}

def bfs(cur_v, target):
    visited[cur_v] = 0
    queue = deque()
    queue.append(cur_v)

    while queue:
        if target in visited:
            break
        cur_v = queue.popleft()
        for next_v in (cur_v-1, cur_v+1, cur_v*2):
            if next_v < 0 or next_v > 100000:
                continue
            if next_v not in visited:
                visited[next_v] = visited[cur_v] + 1
                queue.append(next_v)
    
    return visited[target]

print(bfs(n, k))