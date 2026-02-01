h = int(input())


scores = list(map(int, input().split()))
scores.sort()

med_scores = scores[h //2]
print(med_scores)
