import sys

memo = {}

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        if (a, b, c) not in memo:
            memo[(a, b, c)] = w(20, 20, 20)
        return memo[(a, b, c)]
    
    if a < b and b < c:
        if (a, b, c-1) not in memo:
            memo[(a, b, c-1)] = w(a, b, c-1)
        if (a, b-1, c-1) not in memo:
            memo[(a, b-1, c-1)] = w(a, b-1, c-1)
        if (a, b-1, c) not in memo:
            memo[(a, b-1, c)] = w(a, b-1, c)
        return memo[(a, b, c-1)] + memo[(a, b-1, c-1)] - memo[(a, b-1, c)]
    
    if (a-1, b, c) not in memo:
        memo[(a-1, b, c)] = w(a-1, b, c)
    if (a-1, b-1, c) not in memo:
        memo[(a-1, b-1, c)] = w(a-1, b-1, c)
    if (a-1, b, c-1) not in memo:
        memo[(a-1, b, c-1)] = w(a-1, b, c-1)
    if (a-1, b-1, c-1) not in memo:
        memo[(a-1, b-1, c-1)] = w(a-1, b-1, c-1)

    return memo[(a-1, b, c)] + memo[(a-1, b-1, c)] + memo[(a-1, b, c-1)] - memo[(a-1, b-1, c-1)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")