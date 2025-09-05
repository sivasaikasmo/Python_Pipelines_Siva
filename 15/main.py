import requests
import json


with open(r'D:\Kasmo\Python+Pyspark+Snowflake\Pipelines\Aug 22\15\data.json','r') as f:
    payload=json.load(f)


for i in payload:
    response=requests.post("http://127.0.0.1:8000/etl1", json=i)
    print(response.json())






