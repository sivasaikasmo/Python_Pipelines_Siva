import pandas as pd

def camel_case(stri):
    s=stri.split()
    return ' '.join([x.capitalize() for x in s])

def transform_data(df1):
    
    df1=df1.dropna()
    df1['product_name']=df1['product_name'].apply(camel_case).str.strip()
    df1.loc[:,'price']=df1['price'].apply(lambda x:f'${x:.2f}')
    df1.loc[df1['stock_quantity']<0,'stock_quantity']=0
    df1.loc[:,'stock_status']=df1['stock_quantity'].apply(lambda x:'Low' if x<20 else 'Medium' if x>=20 and x<=50 else 'High')
    df1.loc[:,'Total_value']=df1['stock_quantity']*df1['price'].str[1:].astype(float)

    return df1

