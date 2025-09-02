from pymongo import MongoClient
from config import config_details,config
from src.extract import extract_json
from src.transform import transform
from src.load import load
from sqlalchemy import create_engine 

client = MongoClient(config_details["client"])

db = client[config_details["db"]]

collection = db[config_details["collection"]]

engine = create_engine(f'mysql+mysqlconnector://{config['user']}:{config['password']}@{config['host']}/{config['database']}')

data=extract_json(collection)

df_project,df_technologies,df_milestones,df_team_members=transform(data)

print(load(df_project,df_technologies,df_milestones,df_team_members,engine))



