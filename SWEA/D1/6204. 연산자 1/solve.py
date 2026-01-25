import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
f_N = "{:.2f}".format(N)
print(f_N , ' inch', ' => ', N * 2.54, ' cm')