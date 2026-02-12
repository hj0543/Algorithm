def powerset(level, cursum):
    global result
    if level == N:
        if cursum == S:
            temp = []
            for i in range(N):
                if path[i] == 1:
                    temp.append(arr[i])
            subsets.append(temp)

    else:
        path[level] = 1
        powerset(level + 1, cursum + arr[level])
        path[level] = 0
        powerset(level + 1, cursum)


N, S = map(int, input().split())
arr = list(map(int, input().split()))
path = [0] * N
subsets = []
powerset(0, 0)

if [] in subsets:
    subsets.remove([])

print(len(subsets))