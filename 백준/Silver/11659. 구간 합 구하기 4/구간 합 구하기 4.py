import sys
input = sys.stdin.readline

N, M = map(int, input().split())

nums = list(map(int, input().split())) # 주어진 N개의 수를 리스트로 나타내고



presum = [0] # n번째 까지 숫자를 다 더한 값을 저장할 list

temp = 0


for n in nums:
    temp += n # n번째까지 더한 값
    presum.append(temp) # 을 presum에 넣는다.

for k in range(M):
    i, j = map(int, input().split())

    result = presum[j] - presum[i-1] # j번째 까지 합에서 i-1번째 까지 합을 뺀다.

    print(result)