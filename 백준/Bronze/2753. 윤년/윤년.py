year = int(input())

if year % 4 == 0: 
    # 4의 배수 이면서 400의 배수이면 윤년이다.
    if year % 400 == 0:
        print(1)
    # 4의 배수 이면서 400의 배수아닌데 100의 배수이면 평년이다.
    elif year % 100 == 0:
        print(0)
    # 4의 배수 이면서 400의 배수아닌데 100의 배수가 아니면 윤년이다.
    else:
        print(1)
# 4의 배수가 아니면 평년이다.
else:
    print(0)