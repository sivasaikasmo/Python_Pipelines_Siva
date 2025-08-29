def load_data(df,engine):
    df.to_sql(name='cleaned_inventory',if_exists='replace',con=engine,index=False)
    return 'loaded succesfully'