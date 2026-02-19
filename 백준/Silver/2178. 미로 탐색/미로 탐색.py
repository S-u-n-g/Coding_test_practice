import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maze = [[0] * m for _ in range(n)]

for i in range(n):
    line = sys.stdin.readline().strip()
    for j, v in enumerate(line):
        maze[i][j] = int(v)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * m for _ in range(n)]

def bfs(cur_v):
    visited[cur_v[0]][cur_v[1]] = 1
    queue = deque()
    queue.append(cur_v)

    while queue:
        cur_v = queue.popleft()
        for i in range(len(dx)):
            x, y = cur_v[0]+dx[i], cur_v[1]+dy[i]
            if x >= n or x < 0 or y >= m or y < 0:
                continue
            if maze[x][y] == 1 and visited[x][y] == 0:
                visited[x][y] = visited[cur_v[0]][cur_v[1]] + 1
                queue.append((x, y))

    return visited[n-1][m-1]

print(bfs((0, 0)))