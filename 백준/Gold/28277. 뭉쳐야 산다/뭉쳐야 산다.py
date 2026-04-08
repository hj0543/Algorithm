# 출력방법 수정, import sys; sys ~~~ 추가
import sys
input = sys.stdin.readline

n, q = map(int, input().split())

sets = [set() for _ in range(n+1)]
for i in range(1, n+1):
    s = list(map(int, input().split()))
    sets[i] = set(s[1:])

result = []
for j in range(q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1], query[2]
        
        # 큰 집합을 a로 
        if len(sets[a]) < len(sets[b]):
            sets[a], sets[b] = sets[b], sets[a]
        
        # b는 항상 작은 집합
        for k in sets[b]:
            sets[a].add(k)
            
        sets[b].clear()
        
    else:
        result.append(len(sets[query[1]]))
        
for ans in result:
    print(ans)