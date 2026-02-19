import sys
from collections import deque

n = int(sys.stdin.readline())
land = [[0] * n for _ in range(n)]

for i in range(n):
    line = sys.stdin.readline().strip()
    for j, string in enumerate(line):
        land[i][j] = int(string)

visited = [[False] * n for _ in range(n)]
dummy = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(cur_v):
    visited[cur_v[0]][cur_v[1]] = True
    queue = deque()
    queue.append(cur_v)
    cnt = 1

    while queue:
        cur_v = queue.popleft()
        for i in range(len(dx)):
            next_v = (cur_v[0]+dx[i], cur_v[1]+dy[i])
            x, y = next_v[0], next_v[1]
            # out of range 생각
            if n <= x or x < 0 or n <= y or y < 0:
                continue
            if land[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                cnt += 1
                queue.append((x, y))
    return cnt

for i in range(n):
    for j in range(n):
        if land[i][j] == 1 and not visited[i][j]:
            cnt = bfs((i, j))
            dummy.append(cnt)

print(len(dummy))
for num in sorted(dummy):
    print(num)