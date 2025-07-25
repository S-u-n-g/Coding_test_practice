n = int(input())
result = 0

for _ in range(n):
    arr = []
    word = input()
    check = True
    arr.append(word[0])

    for char in word:
        if char == arr[-1]:
            continue
        if char in arr:
            check = False
            break
        arr.append(char)

    if check:
        result += 1

print(result)