n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
l = 0
r = n - 1
cnt = 0

while l < r:
    if arr[l] + arr[r] == x:
       cnt += 1
       l += 1
    elif arr[l] + arr[r] > x:
        r -= 1
    else:
        l += 1

print(cnt)