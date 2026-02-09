import sys
sys.stdin = open('input.txt', 'r')

##################################################

TC = int(input())
for tc in range(TC):
    words = input().rstrip()

    stack = []

    is_valid = True

    for char in words:
        if char == '(' or char == '{':
            stack.append(char)
        elif char == ')':
            # 스택이 비었거나, 짝이 안 맞으면 실패
            if not stack or stack.pop() != '(':
                is_valid = False
                break
        elif char == '}':
            if not stack or stack.pop() != '{':
                is_valid = False
                break
    
    if stack:
        is_valid = False

    result = 1 if is_valid else 0
    print(f'#{tc+1} {result}')

