import sys
sys.stdin = open('input.txt', 'r')

##################################################

N = int(input())                            # 스위치 개수
S = list(map(int, input().split()))    # [스위치 상태]
students = int(input())                     # 학생 수
data = []                                   # [gender, number]
for i in range(students):
    data.append(list(map(int, input().split())))

switch_init = [0] * 100







