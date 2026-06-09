import requests
import json
import pandas as pd
import os

endpoint = input("가져올 데이터의 이름 : ") #가져올 데이터명
parameters = "?year=2025"
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, f"f1_2025_{endpoint}.json")

def get_f1_data(endpoint,parameters):
    url = f"https://api.openf1.org/v1/{endpoint}{parameters}" 
    response = requests.get(url)               
    return response  

f1_data = get_f1_data(endpoint,parameters)

if f1_data.status_code != 200:
    print(f"API 호출 실패: {f1_data.status_code}")
else:
    f1_data_end = f1_data.json()

    with open(file_path,"w",encoding="utf-8") as file:
        json.dump(f1_data_end,file,indent=4,ensure_ascii=False)
