def load(df1,df2,engine):
    df1.to_sql(name='dynamo_db_2.1',con=engine,if_exists='replace',index=False)
    df2.to_sql(name='dynamo_db_2.2',con=engine,if_exists='replace',index=False)
    return 'Loaded Succesfully'