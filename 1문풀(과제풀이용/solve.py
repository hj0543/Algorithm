import sys
sys.stdin = open('input.txt', 'r')

##################################################

TC = int(input())
for tc in range(TC):
    words = input().rstrip()

    stack = []
    counts1 = 0
    counts2 = 0

    for char in words:

        if char == '(':
            if counts1 >= 0:
                stack.append(char)
                counts1 += 1
            else:
                print(0)
                break

        elif char == ')':
            if counts1 >= 1:
                stack.append(char)
                counts1 -= 1
            else:
                print(0)
                break

        elif char == '{':
            if counts2 >= 0:
                stack.append(char)
                counts2 += 1
            else:
                print(0)
                break

        elif char == '}':
            if counts2 >= 1:
                stack.append(char)
                counts2 -= 1
            else: 
                print(0)
                break

        else:
            continue
    if counts1 == 0 and counts2 == 0:
        print(1)
    else:
        print(0)

    print(stack)    
    # print(f'#{tc+1} {result}')
