import sys
sys.stdin = open('input.txt', 'r')

word = input().split()

word.reverse()
result = ' '.join(word)
print(result)