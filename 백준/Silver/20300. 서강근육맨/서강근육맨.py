import sys

N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))


sort_num = sorted(numbers)


if N % 2 != 0: # N이 홀수라면 
    even_num = []

    for i in range((len(numbers) - 1) // 2): 
        add = sort_num[i] + sort_num[-2-i]
        even_num.append(add)

    if max(even_num) > sort_num[-1]:
        print(max(even_num))
    else:
        print(sort_num[-1])

else: # N이 짝수라면
    odd_num = []

    
    for i in range(len(numbers) // 2 + 1): 
        add = sort_num[i] + sort_num[-1-i]
        odd_num.append(add)
    print(max(odd_num))