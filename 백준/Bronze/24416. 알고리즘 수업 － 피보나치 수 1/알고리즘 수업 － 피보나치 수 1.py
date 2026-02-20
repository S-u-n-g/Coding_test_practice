import sys

n = int(sys.stdin.readline())

cnt = 0
count = 0
f = {}

def fib(n):
    global cnt

    if n == 1 or n == 2:
        cnt += 1
        return 1
    
    return fib(n-1) + fib(n-2)

def fibonacci(n):
    global count
    f[1] = f[2] = 1
    
    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        count += 1
    return f[n]

fib(n)
fibonacci(n)
print(cnt, count)