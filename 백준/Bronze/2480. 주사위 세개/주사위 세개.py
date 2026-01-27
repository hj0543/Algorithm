A, B, C = map(int, input().split())

if A == B == C:
    print(10000 + 1000 * A)
elif (A == B) or (C == A):
    print(1000 + 100 * A)
elif B == C:
    print(1000 + 100 * B)
else:
    if A > B and A > C:
        print(A * 100)
    elif B > A and B > C:
        print(B * 100)
    else:
        print(C * 100)