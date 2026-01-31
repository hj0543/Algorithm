import sys
input = sys.stdin.readline

N = int(input().strip())

# words = []
temp = set()
cnt = 0


for _ in range(N):
    s = input().strip()
    # words.append(s)
    if s == 'ENTER':
        temp.clear()

    else:
        if s not in temp:
            temp.add(s)
            cnt += 1

# total = cnt - words.count('ENTER')
print(cnt)