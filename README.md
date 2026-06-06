# f1-etl
🏎️ F1 ETL Pipeline

F1 팬으로서, 좋아하는 것으로 직접 만들어보고 싶었습니다.
F1의 다양한 데이터를 수집·정제하여 내가 원하는 방식으로 조회하고 시각화하는 것을 목표로 합니다.

<br>
📌 프로젝트 개요
항목내용목적F1 API 데이터를 수집·정제하여 MySQL에 적재하고 대시보드로 시각화기간2026.06 ~ 진행 중상태🟡 진행 중
<br>
🛠 기술 스택
구분기술언어Python라이브러리requests, pandas, SQLAlchemy데이터베이스MySQL (DBeaver)APIOpenF1 API대시보드Grafana 또는 Metabase (예정)
<br>
🏗 아키텍처
OpenF1 API  →  Python  →  MySQL  →  대시보드
 (Extract)   (Transform)  (Load)     (Viz)
<br>
📂 파일 구조
f1-etl/
├── f1.py          # API 호출 및 데이터 수집 (Extract)
└── 기록이미지/    # 학습 과정 스크린샷

Transform, Load, 대시보드 연결은 순차적으로 추가 예정

<br>
✅ 진행 현황

 OpenF1 API 호출 및 JSON 저장
 pandas로 데이터 정제 (Transform)
 MySQL 적재 (Load)
 대시보드 연결 (Viz)
 자동화 (스케줄링)

<br>
🔗 참고

OpenF1 API 공식 문서