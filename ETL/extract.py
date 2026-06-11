import requests
import json
import os
import time


def main(endpoint, year): #메인 실행

    year_group = ["meetings", "sessions"]
    
    if endpoint in year_group:
        data = get_data_by_year(endpoint, year)
    else:
        data = get_data_by_meetings(endpoint, year)
    
    save_json(data, f"f1_{year}_{endpoint}.json")


def get_f1_data(endpoint, params=""): #원하는 api를 호출해서 json파일로 반환함
    api_url = f"https://api.openf1.org/v1/{endpoint}{params}"
    response = requests.get(api_url)

    if response.status_code != 200:
        print(f"불러오기 실패함 이유 : {response.status_code}") #오류 코드 출력
        return None

    else:
        return response.json()
    


def get_meetings_keys(year): #meetings.json에서 meeting_key 가져오기
    meetings = get_f1_data("meetings",f"?year={year}")

    meetings_keys = []

    for meeting in meetings:
        meetings_keys.append(meeting['meeting_key'])

    return meetings_keys


def get_data_by_meetings(endpoint, year): #세션키로 돌면서 원하는 데이터 가져오기
    keys = get_meetings_keys(year)

    data = []
    
    for meetings_key in keys:
        print(f"받는 중... meeting_key={meetings_key}")
        result = get_f1_data(endpoint,f"?meeting_key={meetings_key}")
        if result is not None:
            data.extend(result)
        time.sleep(0.2)

    return data


def get_data_by_year(endpoint, year): #year로 바로 가져올수 있는 meetings, sessions 가져오기
    data = get_f1_data(endpoint,f"?year={year}")

    return data

def save_json(data, filename): #저장
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir,filename)

    with open(file_path,"w",encoding="utf-8") as file:
        json.dump(data,file,ensure_ascii=False,indent=4)

if __name__ == "__main__": #다른 파일에서 import할때 실행안되고 이 파일에서만 실행되게
    main("session_result", 2025)
