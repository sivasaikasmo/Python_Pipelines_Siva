import pandas as pd
from src.extract import extract
from src.transform import transform
from src.load import load
from config import server_conn

mssql = (
    f"mssql+pyodbc://@{server_conn['server']}/{server_conn['database']}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

data=extract()
df=transform(data)
# print(df)
print(load(df,mssql))