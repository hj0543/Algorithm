import sys
sys.stdin = open('input.txt', 'r')

num = int(input())

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

print(factorial(num))

