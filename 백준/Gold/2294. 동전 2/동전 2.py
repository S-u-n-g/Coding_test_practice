import sys

n, k = map(int, sys.stdin.readline().split())
coins = []

for _ in range(n):
    coins.append(int(sys.stdin.readline()))

# dp[i]: i원을 만드는 최소 동전 개수
dp = [sys.maxsize] * (k+1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])