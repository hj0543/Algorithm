import sys
sys.stdin = open('input.txt', 'r')

A = input()
B = input()

print(A)
print(B)
# my_dict = {
#     '가위' : 1,
#     '바위' : 2,
#     '보' : 3,
# }
# print(my_dict['가위'])
# if my_dict[A] - my_dict[B] == 1 | -2:
#     print('Player A가 이겼습니다.', '게임을 계속 진행하겠습니까? (예/아니오)', sep = '\n')
# elif my_dict[B] - my_dict[A] == 1 | -2:
#     print('Player B가 이겼습니다.', '게임을 계속 진행하겠습니까? (예/아니오)', sep = '\n')
# else:
#     print('무승부입니다.')