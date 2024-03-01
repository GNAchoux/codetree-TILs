score_A = input().split()
score_B = input().split()

mathA, engA = int(score_A[0]), int(score_A[1])
mathB, engB = int(score_B[0]), int(score_B[1])

if mathA == mathB:
    if engA > engB:
        print("A")
    else:
        print("B")
elif mathA > mathB:
    print("A")
else:
    print("B")