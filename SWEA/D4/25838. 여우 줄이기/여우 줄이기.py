T = int(input())
for _ in range(T):
    N = int(input())
    word = input()

    stack = []

    for char in word:
        stack.append(char)

        # 마지막에 들어온 문자가 x이고, stack의 길이가 3이상일 때,
        if char == 'x' and len(stack) >= 3:

            # stack의 마지막이 f, o 라면
            if stack[-3] == 'f' and stack[-2] == 'o':
                # stack에서 fox를 지움
                for _ in range(3):
                    stack.pop()

    print(len(stack))