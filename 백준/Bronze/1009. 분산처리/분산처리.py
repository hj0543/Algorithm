T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    result = pow(a, b, 10)
    print(10 if result == 0 else result)