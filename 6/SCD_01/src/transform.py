import pandas as pd

def transform(df1,df2):
    df1.set_index('CustomerID',inplace=True)
    df2.set_index('CustomerID',inplace=True)
    df1.update(df2)
    df1.reset_index(inplace=True)
    df2.reset_index(inplace=True)
    existing_ids = df1['CustomerID'].unique()
    new_rows = df2[~df2['CustomerID'].isin(existing_ids)]
    new_rows['CurrentFlag']=1
    new_rows['Version']=1
    new_rows['PrevLoyaltyTier']=''
    df1=pd.concat([df1,new_rows], ignore_index=True)
    df1=df1.drop('PrevLoyaltyTier',axis=1)

    return df1