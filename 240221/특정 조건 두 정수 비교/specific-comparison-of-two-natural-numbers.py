number = input().split()

a, b = int(number[0]), int(number[1])

if a < b:
    print(1, end=' ')
else:
    print(0, end=' ')

if a==b:
    print(1)
else:
    print(0)