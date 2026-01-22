import sys
sys.stdin = open('input.txt', 'r')

try:
    while True:
        print(input())
except EOFError:
    pass


# for i in range(3):
#     print(input())

'''
A = str(input())
B = str(input())
C = str(input())
print(A)
print(B)
print(C)
'''