import sys
sys.stdin = open("input.txt", "r")

# 문제풀이 2 - 수영장

# [로직전략]
# 1. 외부
# 1-1. 1년 리스트 앞에 0 넣어서 인덱스 정리하기
# 1-2. 초기 최소값 설정 : 연간권
# 2. 백트래킹
# 2-1. 종료조건 : 12월을 넘어가는 경우
# 2-2. 가지치기 : total이 현재 최소값을 넘어가는 경우
# 2-3. 1일, 1달, 3달 다 사용해보고 1년일아 비교


def min_price(month, total_cost):
    global min_cost

    # 종료조건 설정
    if month > 12:
        min_cost = min(min_cost, total_cost)
        return

    # 가지치기
    if total_cost >= min_cost:
        return

    # 1일 이용권
    min_price(month + 1, total_cost + (plan[month] * prices[0]))

    # 1달 이용권
    min_price(month + 1, total_cost + prices[1])

    # 3달 이용권
    min_price(month + 3, total_cost + prices[2])


TC = int(input())
for tc in range(TC):
    prices = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    min_cost = prices[3]
    min_price(1, 0)
    print(f'#{tc+1} {min_cost}')

