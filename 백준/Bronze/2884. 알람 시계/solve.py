A, B = map(int, input().split())

if B >= 45:
    print(A, B-45)
else:
    A = A -1
    if A < 0:
        A = 23 # 00시 일 경우 23시로 지정
    print(A, B + 15)
    # print((A - 1) % 24, B + 15)