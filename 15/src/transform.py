import pandas as pd
import json
from datetime import date

def transform(data):
    df=pd.DataFrame([data])
    df['created_at']=date.today()
    return df