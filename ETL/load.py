import pandas as pd
import os
from sqlalchemy import create_engine
from urllib.parse import quote_plus
from dotenv import load_dotenv

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "clean_drivers.csv")
df = pd.read_csv(file_path)

load_dotenv()  # .env 파일 읽기

user = os.getenv("DB_USER")
password = quote_plus(os.getenv("DB_PASSWORD"))
host = os.getenv("DB_HOST")
db = os.getenv("DB_NAME")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")

df.to_sql("f1_2025_drivers", engine, if_exists="append", index=False)
print("적재 완료!")