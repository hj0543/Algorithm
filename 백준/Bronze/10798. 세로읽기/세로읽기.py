import sys
input = sys.stdin.readline

total = [] # 한 줄을 한 리스트씩 해서 전체를 또 리스트에 담았음

for _ in range(5): # 전체 행의 길이가 5니까
    words = list(map(str, input().rstrip()))
    total.append(words)

result = []

for i in range(15):
    for j in range(5):
        if i < len(total[j]):
            result.append(total[j][i]) # [j][i]로 하여 새로운 리스트에 세로로 입력되게 함

print(''.join(result))