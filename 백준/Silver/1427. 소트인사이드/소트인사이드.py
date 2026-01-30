import sys
N = list(map(str, sys.stdin.readline().strip()))
sort_N = sorted(N)
rev_N = sort_N[::-1]
result = ''.join(rev_N)

print(result)