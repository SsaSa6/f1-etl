#2026-06-08
# 프로젝트 연습
# 문제 : 전체 드라이버 이름 출력 drivers 를 for문으로 
# 돌면서 모든 드라이버의 full_name 을 한 줄씩 출력하세요.

import json

with open("F1 ETL/ETL/f1_data.json", encoding="utf-8") as f:
    drivers = json.load(f)

for driver in drivers:
    print(driver['full_name'])
