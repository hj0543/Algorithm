import sys
input = sys.stdin.readline


A, B = map(int, input().split())


R = min(A, B)

yaksu = [1] # 1 꼭 넣어야한다.. 1은 항상 가지는 공약수니까

for i in range(2, R + 1): # R이 아니라 R + 1까지...
    if A % i == 0 and B % i == 0:
        yaksu.append(i)


G = max(yaksu)
    
L = A * B // G

print(G, L, sep = '\n')