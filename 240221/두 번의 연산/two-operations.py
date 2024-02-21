a = int(input())

if a%2 == 1:
    a += 3
elif a%2 == 0:
    a += 1

if a%3 == 0:
    print(a//3)