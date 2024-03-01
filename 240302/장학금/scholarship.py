score = input().split()
mid, fin = int(score[0]), int(score[1])

if 90 <= mid:
    if 95 <= fin:
        print(100000)
    elif 90 <= fin < 95:
        print(50000)
    else:
        print(0)
else:
    print(0)