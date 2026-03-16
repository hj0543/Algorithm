# 하나의 시점에 몇 가지 경우의 수
# 1일 vs 1달 vs 3달 -> 3가지 경우의 수 -> branch = 3
# 1월 ~ 12월 -> depth = 12

# depth = 12 (12월을 모두 고려한 경우)
# branch = 3 (1일, 1달, 3달)
def recur(month, total_cost):
    global min_answer

    if month > 12:
        min_answer = min(min_answer, total_cost)
        return

    # 현재 시점에서 1일권 vs 1달권 비교가 가능하니 조건문으로 적으면 더 효과적
    if days[month] * cost_d < cost_m:
        recur(month + 1, total_cost + (days[month] * cost_d))
    else:
        recur(month + 1, total_cost + cost_m)

    # 1일권으로 사는 경우
    recur(month + 1, total_cost + (days[month] * cost_day))

    # 1달권으로 사는 경우
    recur(month + 1, total_cost + cost_month1)

    # 3달권으로 사는 경우
    recur(month + 3, total_cost + cost_month3)


T = int(input())


for tc in range(1, T + 1):
    cost_d, cost_m, cost_3m, cost_y = map(int, input().split())
    days = [0] + list(map(int, input().split()))

    min_answer = 21 * 12 * 3000 # 최대금액
    recur(1, 0)
    min_answer = min(min_answer, cost_y)
    print(f'#{tc} {min_answer}')






