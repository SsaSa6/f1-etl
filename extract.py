import requests
import json
import pandas as pd

url = "https://api.openf1.org/v1/drivers?session_key=latest" #api를 호출
response = requests.get(url) #api 결과를 딕셔너리 형태로 저장

if response.status_code != 200: #api호출이 성공적이면 else로 아니면 호출 이유를 설명
    print(f"API 호출 실패: {response.status_code}")
else:
    f1_data = response.json() #response를 json 형태로 변환하여 f1_data에 저장

    with open("f1_data.json", "w", encoding="utf-8") as file: 
        #f1_data를 json 파일로 저장하고 "w"는 쓰기 모드, encoding은 utf-8로 설정
        json.dump(f1_data, file, indent=4, ensure_ascii=False)
        #json.dump()는 f1_data를 file에 json 형식으로 저장, indent는 들여쓰기, ensure_ascii는 비영어 문자를 그대로 저장하도록 설정
