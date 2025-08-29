def load(df1,old_df,engine):
    df1.to_sql(name='SCD_04',con=engine,if_exists='replace',index=False)
    old_df.to_sql(name='SCD_04_History',con=engine,if_exists='replace',index=False)
    return 'Laoded Succesfully'
