from itertools import permutations

def get_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

TC = int(input())
for tc in range(TC):
    N = int(input())
    data = list(map(int, input().split()))
    
    # 회사와 집 좌표
    company = (data[0], data[1])
    home = (data[2], data[3])
    
    # 고객 좌표
    customers = []
    for i in range(4, len(data), 2):
        customers.append((data[i], data[i+1]))

    # 1. 고객 인덱스 리스트 생성
    customer_indices = [i for i in range(N)]

    min_total = float('inf')

    # 2. 모든 순열 탐색
    for p in permutations(customer_indices):
        current_dist = 0
        
        # 회사 -> 첫 번째 고객
        current_dist += get_dist(company, customers[p[0]])
        
        # 고객 -> 고객
        for i in range(N - 1):
            current_dist += get_dist(customers[p[i]], customers[p[i+1]])
            if current_dist >= min_total: # (선택 사항) 중간 최적화
                break
        else:
            # 마지막 고객 -> 집
            current_dist += get_dist(customers[p[-1]], home)
            if current_dist < min_total:
                min_total = current_dist

    print(f'#{tc+1} {min_total}')