import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    sticker = []
    for _ in range(2):
        sticker.append(list(map(int, sys.stdin.readline().split())))

    # i 열에서 위를 뜯었을 때, 아래를 뜯었을 때, 안 뜯었을 때
    # dp는 0~i 열까지 점수 최댓값
    dp0 = [-1] * n
    dp1 = [-1] * n
    dpN = [-1] * n
    dp0[0] = sticker[0][0]
    dp1[0] = sticker[1][0]
    dpN[0] = 0

    for i in range(1, n):
        dp0[i] = sticker[0][i] + max(dp1[i-1], dpN[i-1])
        dp1[i] = sticker[1][i] + max(dp0[i-1], dpN[i-1])
        dpN[i] = max(dp0[i-1], dp1[i-1])

    print(max(max(dp0[-1], dp1[-1]), dpN[-1]))