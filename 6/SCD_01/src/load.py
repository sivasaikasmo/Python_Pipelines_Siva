def load(df1,engine):
    df1.to_sql(name='SCD_01',con=engine,if_exists='replace',index=False)
    return 'Laoded Succesfully'
