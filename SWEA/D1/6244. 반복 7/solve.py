scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

sorted_scores = sorted(scores)

print(sorted_scores)

while sorted_scores < 80:
    sorted_scores.pop()
    print(sorted_scores)
