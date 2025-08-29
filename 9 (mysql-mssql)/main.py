import pandas as pd
from sqlalchemy import create_engine
from config import config
from src.extract import extract
from src.load import load
from config import server_conn


mysql = create_engine(f'mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}/{config['database']}')

mssql = (
    f"mssql+pyodbc://@{server_conn['server']}/{server_conn['database']}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

df1=extract(mysql)


print(load(df1,mssql))




