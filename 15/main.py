import boto3
from config import aws_details
from src.extract import extract
from src.transform import transform
from src.load import load
from config import server_conn


session = boto3.Session(
    aws_access_key_id=aws_details['aws_access_key_id'],
    aws_secret_access_key=aws_details['aws_secret_access_key'],
    region_name="us-east-1")

mssql = (
    f"mssql+pyodbc://@{server_conn['server']}/{server_conn['database']}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

print(extract(session))
df=transform()
load(df,mssql)
