import pandas as pd
import json

df = pd.read_json("f1_data.json") #json 파일을 읽어서 df에 저장
df.info() #df의 정보 출력