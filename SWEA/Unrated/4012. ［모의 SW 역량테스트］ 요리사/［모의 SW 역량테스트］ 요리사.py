from itertools import combinations
  
def synergy(ingredients, matrix):
    score = 0
    # 그룹 내에서 2개를 뽑는 모든 조합
    for i, j in combinations(ingredients, 2):
        score += matrix[i][j] + matrix[j][i]
    return score
  
TC = int(input())
  
for tc in range(TC):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
      
    # 0부터 N-1
    all_ingredients = list(range(N))
    min_diff = float('inf')
  
    # N개 중 N/2개를 뽑는 모든 조합 순회
    for food_a in combinations(all_ingredients, N // 2):
        # A에 속하지 않은 나머지가 food_b
        food_b = [x for x in all_ingredients if x not in food_a]
          
        # 각 음식의 맛 계산
        score_a = synergy(food_a, matrix)
        score_b = synergy(food_b, matrix)
          
        # 차이의 최솟값 갱신
        diff = abs(score_a - score_b)
        if diff < min_diff:
            min_diff = diff
  
    print(f"#{tc+1} {min_diff}")