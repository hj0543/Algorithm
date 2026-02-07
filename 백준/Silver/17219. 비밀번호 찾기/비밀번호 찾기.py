import sys
input = sys.stdin.readline

N, M = map(int,input().split()) # 10 4200
my_password = {}

for _ in range(N):
    site, password = input().split()
    my_password[site] = password

for _ in range(M):
    find_pwd = input().strip()
    print(my_password[find_pwd])