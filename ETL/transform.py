import pandas as pd
import json
import os
import numpy as np

#해야하는거 : 결측치, 이상치, 중복값, 타입 통일, 형식 통일, 필요없는 데이터 제거

def load_json(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir,f"{filename}")

    df = pd.read_json(file_path)

    return df

def clean_drivers():
    df = load_json("f1_2025_drivers.json")

    df = df.drop_duplicates('driver_number')

    df = df.drop(['headshot_url','country_code','meeting_key','session_key'],axis=1)

    return df

def clean_session_result():
    df = load_json("f1_2025_session_result.json")

    df = df.drop(['meeting_key'],axis=1)

def save_clean(clean_data,filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir,f"{filename}")

    clean_data.to_csv(file_path,index = False)

def main():
    df = clean_drivers()
    save_clean(df, "clean_drivers.csv")

if __name__ == "__main__":
    main()