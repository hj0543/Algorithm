N = int(input())

for i in range(1, N + 1):

    words = input().strip()

    if words.isupper():
        loup = '대문자'
    else:
        loup = '소문자'

    print(f'#{i} {words} 는 {loup} 입니다.')