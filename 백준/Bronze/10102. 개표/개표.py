import sys
input = sys.stdin.readline

S = int(input())

votes = list(input())
    

if votes.count('A') > votes.count('B'):
    print('A')
elif votes.count('A') < votes.count('B'):
    print('B')
else:
    print('Tie')