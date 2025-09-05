
from fastapi import FastAPI
from pydantic import BaseModel
from src import transform
from src import load
import uvicorn
from datetime import date
import pandas as pd

app=FastAPI()

server_conn={
    'server':r'SSS-DESKTOP\SQLEXPRESS',\
    'database':'master',\
        }

mssql = (
    f"mssql+pyodbc://@{server_conn['server']}/{server_conn['database']}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

class TaskInput(BaseModel):
    title:str
    status:str


@app.post("/etl1")
def create_task(task_input:TaskInput):
    try:
        dicti=task_input.model_dump()
        df=pd.DataFrame([dicti])
        df['created_at']=date.today()
        df.to_sql(name='api_call',con=mssql,if_exists='append',index=False)
        return {"message": "Loaded Successfully"}
    except Exception as e:
        return {"error":str(e)}



if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)








