import sys
input = sys.stdin.readline

N = int(input())

counts = 1
number = 666
while counts != N:
    number += 1
    if '666' in str(number):
        counts += 1

print(number)