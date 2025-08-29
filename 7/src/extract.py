import pandas as pd
def extract(engine):
    
    sql_query_1='select * from customers'
    df1=pd.read_sql(sql_query_1,engine)
    sql_query_2='select * from order_items'
    df2=pd.read_sql(sql_query_2,engine)
    sql_query_3='select * from orders'
    df3=pd.read_sql(sql_query_3,engine)
    sql_query_4='select * from products'
    df4=pd.read_sql(sql_query_4,engine)
    return df1,df2,df3,df4