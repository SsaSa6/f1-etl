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

def clean_outlier(data):
    iqr1 = np.quantile(0.25)# 제 1분위수
    iqr3 = np.quantile(0.75)# 제 3분위수

def clean_duplicated():
    pass

def clean_drivers():
    df = load_json("f1_2025_drivers.json")

def main():
    pass