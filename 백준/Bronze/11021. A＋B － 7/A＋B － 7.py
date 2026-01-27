T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(f'Case #{i + 1}: {A + B}')

    # for n in range(1, T):
    #     print(f'Case #{n}: {A + B}')
    #     break