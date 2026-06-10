import requests
import json
import os
import time


def main(endpoint, year): #메인 실행

    year_group = ["meetings", "sessions"]
    
    if endpoint in year_group:
        data = get_data_by_year(endpoint, year)
    else:
        data = get_data_by_sessions(endpoint, year)
    
    save_json(data, f"f1_{year}_{endpoint}.json")


def get_f1_data(endpoint, params=""): #원하는 api를 호출해서 json파일로 반환함
    api_url = f"https://api.openf1.org/v1/{endpoint}{params}"
    response = requests.get(api_url)

    if response.status_code != 200:
        print(f"불러오기 실패함 이유 : {response.status_code}") #오류 코드 출력
        return None

    else:
        return response.json()
    


def get_session_keys(year): #sessions.json에서 sessions_key 가져오기
    sessions = get_f1_data("sessions",f"?year={year}")

    session_keys = []

    for session in sessions:
        session_keys.append(session['session_key'])

    return session_keys


def get_data_by_sessions(endpoint, year): #세션키로 돌면서 원하는 데이터 가져오기
    keys = get_session_keys(year)

    data = []
    
    for sessions in keys:
        print(f"받는 중... session_key={sessions}")
        result = get_f1_data(endpoint,f"?session_key={sessions}")
        if result is not None:
            data.extend(result)
        time.sleep(2)

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
    main("drivers", 2025)
