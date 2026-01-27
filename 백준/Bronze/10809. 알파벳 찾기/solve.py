import sys
sys.stdin = open('input.txt', 'r')

S = input()

for char in [chr(i) for i in range(ord('a'), ord('z') + 1)]:
    print(S.find(char), end = ' ')

