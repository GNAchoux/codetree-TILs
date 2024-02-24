score_A = input().split()
math_A, eng_A = int(score_A[0]), int(score_A[1])

score_B = input().split()
math_B, eng_B = int(score_B[0]), int(score_B[1])

if math_A > math_B and eng_A > eng_B:
    print(1)
else:
    print(0)