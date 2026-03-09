from itertools import combinations

while True:
    numbers = list(map(int, input().split()))

    if numbers == [0]:
        break

    k = numbers[0]
    S = numbers[1:]

    for combo in combinations(S, 6):
        print(*combo)

    print()