


heights.append(0)

stack = []
max_area = 0

for i in range(N + 1):
    # 스택이 존재하고, 현재 막대 높이가 스택 top(이전 막대)보다 낮아지는 순간
    while stack and heights[stack[-1]] > heights[i]:
        # 꺼낸 막대의 높이가 직사각형의 '높이'가 됨
        h = heights[stack.pop()]
        
        # 너비(w) 계산 logic:
        # 1. 스택이 비었다면: 현재 i번째 막대 이전까지가 모두 이 높이(h)보다 큼
        # 2. 스택에 값이 있다면: 현재 i와 '새로운 top' 사이의 간격이 너비가 됨
        w = i if not stack else i - stack[-1] - 1
        
        # 최댓값 갱신
        if max_area < h * w:
            max_area = h * w
            
    # 현재 인덱스를 스택에 추가
    stack.append(i)

print(max_area)