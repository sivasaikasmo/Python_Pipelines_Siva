import pandas as pd
from sqlalchemy import create_engine
from config import config
from src.extract import extract
from src.transform import transform_data
from src.load import load


engine = create_engine(f'mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}/{config['database']}')


df1,df2=extract(engine)

df1=transform_data(df1,df2)

print(load(df1,engine))




