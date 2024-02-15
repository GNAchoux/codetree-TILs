money = int(input())

if 3000 <= money <= 10000:
    print("book")
elif 1000 <= money < 3000:
    print("mask")
elif 500 <= money < 1000:
    print("pen")
else:
    print("no")