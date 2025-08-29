from src.extract import extract
from src.transform import transform_data
from src.load import load_data
import pandas as pd
from sqlalchemy import create_engine
import pyodbc


server = r'SSS-DESKTOP\SQLEXPRESS'
database = 'master'

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine=create_engine(connection_string)

def main():
    df1=extract()
    df1=transform_data(df1)
    print(load_data(df1,engine))

if __name__=='__main__':
    main()




