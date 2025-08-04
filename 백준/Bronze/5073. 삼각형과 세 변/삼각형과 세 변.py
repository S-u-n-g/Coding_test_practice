a, b, c = map(int, input().split())

while not a == b == c == 0:
    max_len = max([a, b, c])
    if max_len >= (a + b + c - max_len):
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")

    a, b, c = map(int, input().split())