scores = [] # 점수들을 받아와서 담을 빈 리스트 생성

for _ in range(5):
    N = int(input())
    scores.append(N) # 리스트에 점수들을 담음

for i in range(len(scores)): # 점수들 갯수만큼
    if scores[i] < 40: # 점수가 40점 미만이면
        scores[i] = 40 # 그 점수를 40점으로 만들어줌

print(sum(scores) // 5) # 덮어씐 점수 리스트의 평균 구하기