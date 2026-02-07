import sys
input = sys.stdin.readline

N = int(input())
words = [str(input().rstrip()) for _ in range(N)]
words = list(set(words))

words.sort(key=lambda x: (len(x), x))

for i in words:
    print(i)