import pandas as pd
from sqlalchemy import create_engine
from config import config
from src.extract import extract
from src.transform import transform
from src.load import load


engine = create_engine(f'mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}/{config['database']}')


df1,df2,df3,df4=extract(engine)

trans_analysis =transform(df1,df2,df3,df4)

print(load(trans_analysis,engine))




