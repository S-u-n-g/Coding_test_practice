from collections import deque
import sys

n = int(sys.stdin.readline())
queue = deque()

for _ in range(n):
    instruct = list(map(str, sys.stdin.readline().rstrip().split()))
    if instruct[0] == 'push':
        queue.append(int(instruct[1]))
    elif instruct[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif instruct[0] == 'size':
        print(len(queue))
    elif instruct[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif instruct[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif instruct[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
