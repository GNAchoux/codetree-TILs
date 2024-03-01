num = input().split()
a, b, c = int(num[0]), int(num[1]), int(num[2])

if a > b:
    if a > c:
        print(a)
    elif a < c and b > c:
        print(b)
    else:
        print(c)
elif a < b:
    if b > c:
        print(b)
    elif b < c and a > c:
        print(a)
    else:
        print(c)