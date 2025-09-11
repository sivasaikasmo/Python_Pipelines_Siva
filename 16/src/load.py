import pandas as pd

def load(data,engine):
    df1=pd.DataFrame(data)
    df1.to_sql(name='Gmail_Data',con=engine,if_exists='replace',index=False)


