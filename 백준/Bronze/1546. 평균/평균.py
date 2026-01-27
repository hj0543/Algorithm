N = int(input())
scores = list(map(int, input().split()))

# 내장함수 이용 x 최댓값 출력
sorted_scores = sorted(scores)
max_score = sorted_scores[-1]

jojak = []

for i in range(N):
    fixed_scores = scores[i] / max_score * 100
    jojak.append(fixed_scores)

average = sum(jojak) / N
print(average)