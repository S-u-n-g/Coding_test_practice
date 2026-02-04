import sys

n = int(sys.stdin.readline())
queue = list(map(int, sys.stdin.readline().split()))
queue.reverse()
stack = []
num = 1

while stack or queue:
    if queue:
        if queue[-1] == num:
            queue.pop()
            num += 1
        elif num not in stack:
            stack.append(queue[-1])
            queue.pop()
        elif stack[-1] == num:
            stack.pop()
            num += 1
        else:
            print("Sad")
            exit()
    else:
        if stack[-1] == num:
            stack.pop()
            num += 1
        else:
            print("Sad")
            exit()
print("Nice")