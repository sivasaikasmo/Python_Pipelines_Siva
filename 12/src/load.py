def load(df1,df2,df3,df4,engine):
    df1.to_sql(name='dynamo_db_1',con=engine,if_exists='replace',index=False)
    df2.to_sql(name='dynamo_db_2',con=engine,if_exists='replace',index=False)
    df3.to_sql(name='dynamo_db_3',con=engine,if_exists='replace',index=False)
    df4.to_sql(name='dynamo_db_4',con=engine,if_exists='replace',index=False)
    return 'Loaded Succesfully'