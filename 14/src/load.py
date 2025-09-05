def load(df,engine):
    df.to_sql(name='twitter_data',con=engine,if_exists='replace',index=False)
    return 'Loaded Succesfully'