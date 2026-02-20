import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    cur_x, cur_y = map(int, sys.stdin.readline().split())
    target_x, target_y = map(int, sys.stdin.readline().split())

    visited = [[0] * n for _ in range(n)]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]

    def bfs(cur_v, target_v):
        if cur_v == target_v:
            return 0
        visited[cur_v[0]][cur_v[1]] = 0
        queue = deque()
        queue.append(cur_v)

        while queue:
            cur_v = queue.popleft()
            for i in range(len(dx)):
                next_x = cur_v[0] + dx[i]
                next_y = cur_v[1] + dy[i]
                if next_x >= n or next_x < 0 or next_y >= n or next_y < 0:
                    continue
                if visited[next_x][next_y] == 0:
                    visited[next_x][next_y] = visited[cur_v[0]][cur_v[1]] + 1
                    queue.append((next_x, next_y))
                    if next_x == target_v[0] and next_y == target_v[1]:
                        return visited[target_v[0]][target_v[1]]

        return visited[target_v[0]][target_v[1]]

    print(bfs((cur_x, cur_y), (target_x, target_y)))