import requests
import json

url = "https://api.openf1.org/v1/drivers?session_key=latest"
response = requests.get(url)

if response.status_code != 200:
    print(f"API 호출 실패: {response.status_code}")
else:
    f1_data = response.json()
    print(f"드라이버 수: {len(f1_data)}")
    print(f"첫 번째 항목: {f1_data[0]}")

    with open("f1_data.json", "w", encoding="utf-8") as file:
        json.dump(f1_data, file, indent=4, ensure_ascii=False)

    print("저장 완료!")