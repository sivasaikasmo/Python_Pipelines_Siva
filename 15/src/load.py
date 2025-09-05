def load(df):
    server_conn={
    'server':r'SSS-DESKTOP\SQLEXPRESS',\
    'database':'master',\
    }
    mssql = (
    f"mssql+pyodbc://@{server_conn['server']}/{server_conn['database']}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes")
    df.to_sql(name='api_call',con=mssql,if_exists='append',index=False)