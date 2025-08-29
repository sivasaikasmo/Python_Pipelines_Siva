def load(df,engine):
    df.to_sql(name='dim_customers_scd2',con=engine,if_exists='replace',index=False)
    return 'Loaded Succesfully'