import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def check_like(r, c, like_students):
    counts = 0
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:
            if classroom[nr][nc] in like_students:
                counts += 1
    return counts

def check_empty(r, c):
    counts = 0
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and classroom[nr][nc] == 0:
            counts += 1
    return counts

# --------------------------------------------------------

N = int(input())

data = [list(map(int, input().split())) for _ in range(N * N)]
classroom = [[0] * N for _ in range((N))]

# 선호정보를 딕셔너리로 저장
student_likes = {}

for k in range(N ** 2):
    num = data[k][0]
    like = data[k][1:]
    student_likes[num] = like

    best_r, best_c = -1, -1
    max_like_counts = -1
    max_empty_counts = -1

    for i in range(N):
        for j in range(N):
            if classroom[i][j] == 0:
                like_counts = check_like(i, j, like)
                empty_counts = check_empty(i, j)

                # 좋아하는 학생
                if like_counts > max_like_counts:
                    max_like_counts, max_empty_counts = like_counts, empty_counts
                    best_r, best_c = i, j
                
                # 좋아하는 학생 수는 같을 때, 빈칸
                elif like_counts == max_like_counts:
                    if empty_counts > max_empty_counts:
                        max_empty_counts = empty_counts
                        best_r, best_c = i, j

                    # 빈칸도 같을 때, 행 번호 
                    elif empty_counts == max_empty_counts:
                        if i < best_r or (i == best_r and j < best_c):
                            best_r, best_c = i, j                

    classroom[best_r][best_c] = num


# 인접한 자리에 좋아하는 학생 수에 따른 만족도
score_map = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

satisfication_score = 0

for i in range(N):
    for j in range(N):
        student_num = classroom[i][j]
        like_cnt = check_like(i, j, student_likes[student_num])
        satisfication_score += score_map[like_cnt]

print(satisfication_score)