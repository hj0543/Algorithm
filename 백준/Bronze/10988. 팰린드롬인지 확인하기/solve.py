import sys
sys.stdin = open('input.txt', 'r')

S = input()

palin = list(S)

rev_palin = palin[::-1]

if palin == rev_palin:
    print(1)
else:
    print(0)







