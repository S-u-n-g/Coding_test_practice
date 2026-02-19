import sys
sys.setrecursionlimit(10**5)

def dfs(cur_v):
    visited[cur_v[0]][cur_v[1]] = True
    for i in range(len(dx)):
        x, y = (cur_v[0]+dx[i], cur_v[1]+dy[i])
        if x >= n or x < 0 or y >= m or y < 0:
            continue
        if graph[x][y] == 1 and not visited[x][y]:
            dfs((x, y))


t = int(sys.stdin.readline())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
results = []

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs((i, j))
                cnt += 1
    results.append(cnt)

for result in results:
    print(result)