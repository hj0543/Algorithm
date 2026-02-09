import sys
input = sys.stdin.readline

while True:
    sentence = list(map(str, input().rstrip()))

    if sentence[0] == '.':
        break

    stack = []
    for s in sentence:
        if s == '(' or s == '[':
            stack.append(s)

        elif s == ')':
            if not stack or stack[-1] != '(':
                print('no')
                break
            stack.pop()

        elif s == ']':
            if not stack or stack[-1] != '[':
                print('no')
                break
            stack.pop()
    else:
        if not stack:
            print('yes')
        else:
            print('no')