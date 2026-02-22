H, W = map(int, input().split())
sky= []
for i in range(H):
    sky.append(list(map(str,input().rstrip())))

# 구름이 뜬 시간을 기록할 리스트
time_stamp = []
for i in range(H):
    time_stamp.append([-1] * W)


t = 0
while t < W:
    for i in range(H):
        for j in range(W - 1, -1, -1):      # 이 부분 해결못해서 도움 받음 range(W)가 아님..
            if sky[i][j] == 'c':
                if t == 0:
                    time_stamp[i][j] = 0
                elif time_stamp[i][j] == -1:
                    time_stamp[i][j] = t
                if j + 1 < W:
                    sky[i][j], sky[i][j+1] = '.', 'c'
                else:
                    sky[i][j] = '.'
    t += 1

for i in range(H):
    print(*time_stamp[i])

# AI 도움 받은 부분
'''
for 문의 문법을 잘못 이해하신 것은 아니지만, "배열을 훑는 순서"와 "구름이 이동하는 방향"이 같아서 발생하는 논리적 오류가 있습니다.

이 현상을 흔히 "데이터 덮어쓰기(Cascading Update)" 문제라고 합니다.

틀린 이유: 구름이 순간이동을 합니다!
작성하신 코드는 왼쪽(j=0)부터 오른쪽(j=W-1)으로 가면서 구름을 한 칸씩 오른쪽으로 밉니다.

가령, 구름이 맨 앞(j=0)에 하나 있다고 가정해 봅시다 (c . . .).

j=0일 때:

sky[i][0]이 c입니다.
이것을 sky[i][1]로 옮깁니다. (. c . .)

j=1일 때 (바로 다음 반복):

방금 옮겨온 sky[i][1]을 봅니다. 어? c가 있네요.
이것을 또 sky[i][2]로 옮깁니다. (. . c .)

j=2일 때:

방금 옮겨온 sky[i][2]를 또 봅니다.
이것을 sky[i][3]으로 옮깁니다. (. . . c)
결과: t=0인 한 번의 시간 동안 구름이 한 칸만 가는 게 아니라, 배열의 끝까지 순식간에 이동해버립니다.

해결 방법 (간단한 수정)
오른쪽으로 밀어야 한다면, 오른쪽 끝에서부터 왼쪽으로(Reverse) 검사해야 합니다. 그래야 방금 옮긴 구름을 이번 for 문에서 다시 마주치지 않습니다.
'''