import sys
sys.stdin = open('input.txt', 'r')

# 10163
import sys
input = sys.stdin.readline

N = int(input())

# init = []
# for _ in range(1001):
#     init.append([0] * 1001)

# 색종이 초기설정
paper = [[0] * 1001 for _ in range(1001)]


# 모든 색종이를 칠하기 -> 기존 색종이를 덮어씌우는게 포인트다.. 문제 안읽고 중첩으로 풀었네..
for k in range(1, N + 1):

    x, y, w, h = map(int, input().split())

    for j in range(y, y + h): # 이 부분 슬라이싱 으로 수정함.
        paper[j][x:(x + w)] = [k] * w # j행 x 가로 범위만큼 k로 채운다.


# # 각 보이는 색종이 넓이 저장할 리스트
# total = [0] * (N + 1)    


# 전체 색종이에 보이는 번호를 그 리스트 번호에 담는다
# 제약조건 없애기 위해 변수선언 삭제
# 제약 조건 없애기 위해 for문 범위 수정
for i in range(1, N + 1):
    total = 0
    for j in range(1001):
        total += paper[j].count(i) 

    print(total)

    

