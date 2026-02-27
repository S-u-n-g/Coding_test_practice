import sys
from collections import deque

c, r, h = map(int, sys.stdin.readline().split())
box = []

for _ in range(h):
    b = []
    for _ in range(r):
        b.append(list(map(int, sys.stdin.readline().split())))
    box.append(b)

visited = [[[0] * c for _ in range(r)] for _ in range(h)]
ripe = []

for i in range(h):
    for j in range(r):
        for k in range(c):
            if box[i][j][k] == -1:
                visited[i][j][k] = -1
            elif box[i][j][k] == 1:
                ripe.append((i, j, k))

check = True
for i in range(h):
    for j in range(r):
        for k in range(c):
            if visited[i][j][k] == 0:
                check = False

if check:
    print(0)
    sys.exit(0)

def bfs(cur_list):
    cnt = 1
    dz = [0, 0, 0, 0, 1, -1]
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    for cur_v in cur_list:
        cur_z, cur_x, cur_y = cur_v[0], cur_v[1], cur_v[2]
        visited[cur_z][cur_x][cur_y] = cnt

    queue = deque()
    queue.append(cur_list)

    while queue:
        cur_list = queue.popleft()
        if cur_list == []:
            break
        cnt += 1
        next_list = []
        for cur_v in cur_list:
            cur_z, cur_x, cur_y = cur_v[0], cur_v[1], cur_v[2]
            for x, y, z in zip(dx, dy, dz):
                next_x = cur_x + x
                next_y = cur_y + y
                next_z = cur_z + z
                if next_x >= r or next_x < 0 or next_y >= c or next_y < 0 or next_z >= h or next_z < 0:
                    continue
                if visited[next_z][next_x][next_y] == 0:
                    visited[next_z][next_x][next_y] = cnt
                    next_list.append((next_z, next_x, next_y))
        queue.append(next_list)
    
    for i in range(h):
        for j in range(r):
            for k in range(c):
                if visited[i][j][k] == 0:
                    return -1
    return cnt-2

print(bfs(ripe))