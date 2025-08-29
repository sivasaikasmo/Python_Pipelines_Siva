import pandas as pd
def extract(engine):
    
    sql_query_1='select * from customers_snapshot'
    df1=pd.read_sql(sql_query_1,engine,index_col=None)
    return df1