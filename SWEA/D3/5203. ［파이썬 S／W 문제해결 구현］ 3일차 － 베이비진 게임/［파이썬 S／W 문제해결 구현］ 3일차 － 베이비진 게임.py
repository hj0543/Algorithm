
def check_babygin(player_counts):
    for i in range(10):
        # Triplet 체크 (같은 숫자 3개)
        if player_counts[i] >= 3:
            return True
        
        # Run 체크 (연속된 숫자 3개)
        if i <= 7:
            if player_counts[i] >= 1 and player_counts[i+1] >= 1 and player_counts[i+2] >= 1:
                return True
    return False

TC = int(input())

for tc in range(TC):
    cards = list(map(int, input().split()))
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0

    for i in range(len(cards)):
        if i % 2 == 0:
            p1[cards[i]] += 1
            # 카드가 3장 이상일 때부터 승패 체크 가능
            if i >= 4 and check_babygin(p1):
                winner = 1
                break
        else:
            p2[cards[i]] += 1
            if i >= 5 and check_babygin(p2):
                winner = 2
                break

    print(f"#{tc+1} {winner}")