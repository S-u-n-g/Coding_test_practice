import sys

n  = int(sys.stdin.readline())
stair = [int(sys.stdin.readline()) for _ in range(n)]

if n == 1:
    print(stair[0])
    sys.exit()
elif n == 2:
    print(stair[0] + stair[1])
    sys.exit()

dp = [0] * n 

dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n):
    dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[-1])