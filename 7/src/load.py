def load(df,engine):
    df.to_sql(name='transformed_1',con=engine,if_exists='replace')
    return 'Loaded Succesfully'