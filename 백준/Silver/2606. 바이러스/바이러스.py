import sys
from collections import deque

length_of_computers = int(sys.stdin.readline())
length_of_pairs = int(sys.stdin.readline())

graph = {}
visited = []

for i in range(1, length_of_computers+1):
    graph[i] = []

for _ in range(length_of_pairs):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(cur_v):
    visited.append(cur_v)
    queue = deque()
    queue.append(cur_v)

    while queue:
        cur_v = queue.popleft()
        for next_v in graph[cur_v]:
            if next_v not in visited:
                visited.append(next_v)
                queue.append(next_v)    

bfs(1)

print(len(visited) - 1)