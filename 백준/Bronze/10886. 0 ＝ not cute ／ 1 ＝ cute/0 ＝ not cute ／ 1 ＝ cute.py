import sys
input = sys.stdin.readline

S = int(input())

numbers = []

for i in range(S):
    num = int(input())
    
    numbers.append(num)

if numbers.count(1) > numbers.count(0):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')