T = int(input())
 
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    # print(sorted_data)
 
    # 두 음의 차이 계산
    gap1 = (b - a) % 12
    gap2 = (c - b) % 12
 
    # 첫 번째 간격 4, 두 번째 간격 3 이면 메이저 기본형 M
    if gap1 == 4 and gap2 == 3:
        ans = "M"
     
    # 첫 번째 간격 3, 두 번째 간격 5 이면 메이저 기본형 : M/첫 번째로 낮은 소리
    elif gap1 == 3 and gap2 == 5:
        ans = f"M/{a}"
     
    # 첫 번째 간격 5, 두 번째 간격 4 이면 메이저 2전위 : M/첫 번째로 낮은 소리
    elif gap1 == 5 and gap2 == 4:
        ans = f"M/{a}"
     
    # 그 외 : N
    else:
        ans = "N"
 
    print(f"#{tc} {ans}")
                           