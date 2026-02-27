import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    if n == 1 or n == 2 or n == 3:
        print(1)
        continue
    elif n == 4 or n == 5:
        print(2)
        continue

    # dp[i]: i 번째 정삼각형의 한 변의 길이
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2

    for i in range(6, n+1):
        dp[i] = dp[i-5] + dp[i-1]
    
    print(dp[n])