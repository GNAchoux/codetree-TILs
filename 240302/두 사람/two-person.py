A = input().split()
B = input().split()

ageA, ageB = int(A[0]), int(B[0])
sexA, sexB = A[1], B[1]

if ageA>=19 and sexA == "M" or ageB>=19 and sexB == "M":
    print(1)
else:
    print(0)