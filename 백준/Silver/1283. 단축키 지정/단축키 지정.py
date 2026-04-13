import sys
input = sys.stdin.readline

n = int(input())
used = set()

for _ in range(n):
    s = input().rstrip()

    first_candidates = []
    all_candidates = []

    # 전체 후보 수집
    for i, char in enumerate(s):
        if char == ' ':
            continue

        all_candidates.append(i)

        if i == 0 or s[i - 1] == ' ':
            first_candidates.append(i)

    # 우선순위대로 합치기
    order = first_candidates + all_candidates

    chosen = -1
    checked = []

    for idx in order:
        if idx in checked:
            continue
        checked.append(idx)

        char = s[idx].lower()
        if char not in used:
            used.add(char)
            chosen = idx
            break

    if chosen != -1:
        s = s[:chosen] + '[' + s[chosen] + ']' + s[chosen + 1:]

    print(s)