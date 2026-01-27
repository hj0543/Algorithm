from datetime import datetime, timedelta

# UTC 현재 시간 구하기
now_utc = datetime.utcnow()

# 9시간 더해서 KST 만들기
now_kst = now_utc + timedelta(hours=9)

# YYYY-MM-DD 형식으로 출력
print(now_kst.strftime("%Y-%m-%d"))
