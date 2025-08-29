from config import server_conn
from src.extract import extract
from src.transform import transform
from src.load import load
from sqlalchemy import create_engine


connection_string = (
    f"mssql+pyodbc://@{server_conn['server']}/{server_conn['database']}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

df1,df2=extract()
df1=transform(df1,df2)
print(load(df1,connection_string))


