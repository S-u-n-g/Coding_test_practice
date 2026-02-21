import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
box = []

for _ in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))

visited = [[0] * m for _ in range(n)]
ripe = []

for i in range(n):
    for j in range(m):
        if box[i][j] == -1:
            visited[i][j] = -1
        elif box[i][j] == 1:
            ripe.append((i, j))

check = True
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            check = False

if check:
    print(0)
    sys.exit(0)

def bfs(cur_list):
    cnt = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for cur_v in cur_list:
        cur_x, cur_y = cur_v[0], cur_v[1]
        visited[cur_x][cur_y] = cnt

    queue = deque()
    queue.append(cur_list)

    while queue:
        cur_list = queue.popleft()
        if cur_list == []:
            break
        cnt += 1
        next_list = []
        for cur_v in cur_list:
            cur_x, cur_y = cur_v[0], cur_v[1]
            for x, y in zip(dx, dy):
                next_x = cur_x + x
                next_y = cur_y + y
                if next_x >= n or next_x < 0 or next_y >= m or next_y < 0:
                    continue
                if visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = cnt
                    next_list.append((next_x, next_y))
        queue.append(next_list)
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0:
                return -1
    return cnt-2

print(bfs(ripe))