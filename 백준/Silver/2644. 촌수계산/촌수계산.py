import sys
from collections import deque

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
family = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)

visited = {}


def bfs(cur_v, target_v):
    visited[cur_v] = 0
    queue = deque()
    queue.append(cur_v)

    while queue:
        cur_v = queue.popleft()
        for next_v in family[cur_v]:
            if next_v not in visited:
                visited[next_v] = visited[cur_v] + 1
                queue.append(next_v)

    if target_v not in visited:
        return -1

    return visited[target_v]

print(bfs(a, b))