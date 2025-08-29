# Task 4: SCD Type-4 (Separate Historical Table)
# Identify columns for historical tracking in a separate table (e.g., SubscriptionStart, SubscriptionEnd).
# Insert all subscription updates into Customer_Subscription_History.
# Ensure historical records are preserved and can be queried independently.


import pandas as pd

def transform_data(df1,df2):
    merged=pd.merge(df1,df2,on='CustomerID',how='left',suffixes=('','_new'))
    old_df=merged.iloc[0:0]
    for i in ['FirstName','LastName','Email','Phone','Address','LoyaltyTier','SubscriptionStart']:
        j=merged.loc[((merged[i]!=merged[i+'_new']) & (merged[i+'_new'].notnull()))]
        old_df=pd.concat([old_df,j])
    # print(df1)
    old_df=old_df.drop_duplicates()
    df1.loc[df1['CustomerID'].isin(old_df['CustomerID']),'Version']+=1
    df1.set_index('CustomerID',inplace=True)
    df2.set_index('CustomerID',inplace=True)
    df1.update(df2)
    df1.reset_index(inplace=True)
    df2.reset_index(inplace=True)
    # print(df1)
    old_df['CurrentFlag']=0
    old_df['Version']=1
    old_df=old_df.loc[:,old_df.columns.isin(df1.columns)]
    existing_ids = df1['CustomerID'].unique()
    new_rows = df2[~df2['CustomerID'].isin(existing_ids)]
    new_rows['CurrentFlag']=1
    new_rows['Version']=1
    new_rows['PrevLoyaltyTier']=''
    df1=pd.concat([df1,new_rows], ignore_index=True)

    return df1,old_df

