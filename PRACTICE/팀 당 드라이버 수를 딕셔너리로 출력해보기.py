#2026-06-08
# 프로젝트 연습
# 문제 : 팀 당 드라이버가 몇명인지 딕셔너리로 만들어서 출력해보기
# 솔직히 아직 잘 모르겠지만 풀긴함 열심히 해보자

import json

with open("F1 ETL/PRACTICE/f1_data.json",encoding="utf-8") as f:
    drivers = json.load(f)


result = {}
for driver in drivers:
    result[driver['team_name']] = 0

for driver in drivers:
    if driver['team_name'] in result:
        result[driver['team_name']] += 1
print(result)