import pandas as pd
def extract(engine):
    
    sql_query_1='select * from customers_snapshot'
    df2=pd.read_sql(sql_query_1,engine,index_col=None)
    sql_query_2='select * from dim_customers_before'
    df1=pd.read_sql(sql_query_2,engine,index_col=None)
    return df1,df2