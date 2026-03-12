import sys
sys.stdin = open('input.txt', 'r')

##################################################

print(sorted(map(int, input().split()))[500000])