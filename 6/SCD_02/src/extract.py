import pandas as pd

def extract():
    df1=pd.read_csv('Aug 25\\SCD_02\\src\\Customer_Master.csv')
    df2=pd.read_csv('Aug 25\\SCD_02\\src\\Customer_Updates.csv')
    return df1,df2
