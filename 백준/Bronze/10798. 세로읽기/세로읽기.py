arr = [[-1] * 15 for _ in range(5)]
for i in range(5):
    arr[i] = list(input())

for j in range(15):
    for i in range(5):
        if len(arr[i]) <= j:
            continue
        print(arr[i][j], end="")