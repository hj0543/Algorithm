#import sys
from solve import init, addTower, runSimulation

CMD_ADD = 200
CMD_RUN = 300

def run():
	okay = False
	N = int(input())
	mMap = [[0]*N for _ in range(N)]

	for y in range(N):
		input_iter = iter(input().split())
		for x in range(N):
			mMap[y][x] = int(next(input_iter))

	init(N, mMap)

	okay = True
	Q = int(input())

	for q in range(Q):
		input_iter = iter(input().split())
		cmd = int(next(input_iter))

		if cmd == CMD_ADD:
			mRow = int(next(input_iter))
			mCol = int(next(input_iter))
			mInterval = int(next(input_iter))
			addTower(mRow, mCol, mInterval)

		elif cmd == CMD_RUN:
			M = int(next(input_iter))
			mInterval = int(next(input_iter))
			mHP = int(next(input_iter))
			mRetTs = [0 for _ in range(M)]
			mRetHP = [0 for _ in range(M)]

			runSimulation(M, mInterval, mHP, mRetTs, mRetHP)

			for i in range(M):
				x = int(next(input_iter))
				if mRetTs[i] != x:
					okay = False

			for i in range(M):
				x = int(next(input_iter))
				if mRetHP[i] != x:
					okay = False
		else:
			okay = False

	return okay

import sys
sys.stdin = open('input.txt', 'r')

T, MARK = map(int, input().split())

for tc in range(1, T + 1):
	score = MARK if run() else 0
	print("#%d %d" % (tc, score))