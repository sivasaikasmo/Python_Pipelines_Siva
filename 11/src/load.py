def load(df1,df2,engine):
    df1.to_sql(name='project_details',con=engine,if_exists='replace',index=False)
    df2.to_sql(name='project_technologies',con=engine,if_exists='replace',index=False)

    return 'Loaded Succesfully'