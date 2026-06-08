#2026-06-08
# 프로젝트 연습
# 문제 : McLaren 드라이버들의 이름만 출력

import json

with open("F1 ETL/PRACTICE/f1_data.json",encoding="utf-8") as f:
    drivers = json.load(f)

for driver in drivers:
    if driver["team_name"]=="McLaren":
        print(driver["full_name"])