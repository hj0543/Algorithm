def solve(idx, current_sum):
    global min_diff
  
    # 가지치기
    if current_sum >= b:
        min_diff = min(min_diff, current_sum - b)
        return
  
    # 종료조건
    if idx == n:
        return
  
    # 현재 점원을 포함하는 경우
    solve(idx + 1, current_sum + heights[idx])
  
    # 현재 점원을 포함하지 않는 경우
    solve(idx + 1, current_sum)
  
  
TC = int(input())
for tc in range(TC):
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
  
    min_diff = float('inf')
  
    solve(0, 0)
  
    print(f"#{tc+1} {min_diff}")