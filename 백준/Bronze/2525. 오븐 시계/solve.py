A, B = map(int, input().split())
C = int(input())

if B + C < 60:
    print(A, B + C)
else:
    A = A + ((B + C) // 60)
    if A >= 24:
        A = A % 24 # 00시 넘어갈 때 써먹자...
    print(A, ((B + C) % 60))