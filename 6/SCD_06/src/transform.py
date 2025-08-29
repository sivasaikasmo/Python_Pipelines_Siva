# Combine all previous tasks into a single ETL workflow:
# Overwrite Email/Phone (Type-1)
# Maintain address history (Type-2)
# Track previous loyalty tier (Type-3)
# Insert subscription history into a separate table (Type-4)
# Insert new customers into the master table.
# Validate that all tables reflect the correct historical and current state.


import pandas as pd
from datetime import datetime

def transform_data(df1,df2):

    # SCD - 01
    df1.set_index('CustomerID',inplace=True)
    df2.set_index('CustomerID',inplace=True)
    df1.update(df2[['Email','Phone']])
    df1.reset_index(inplace=True)
    df2.reset_index(inplace=True)
    
    #SCD - 02

    merged=pd.merge(df1,df2,on='CustomerID',how='left',suffixes=('','_new'))
    changed=merged.loc[((merged['Address']!=merged['Address_new']) & (merged['Address_new'].notnull()))]
    now=datetime.now()
    df1.loc[df1['CustomerID'].isin(changed['CustomerID']) & df1['CurrentFlag'],
    ['expiry_date', 'CurrentFlag']] = [now, 0]
    changed['effective_date']=now
    changed['current_flag']=1
    version_map = df1.groupby('CustomerID')['Version'].max().to_dict()
    changed['Version'] = changed['CustomerID'].map(version_map).fillna(0).astype(int) + 1
    changed['PrevLoyaltyTier']=''
    changed['expiry_date']=''
    changed=changed[['CustomerID','FirstName_new','LastName_new','Email_new','Phone_new','Address_new','current_flag','Version','LoyaltyTier_new',\
                'PrevLoyaltyTier','SubscriptionStart_new','SubscriptionEnd_new','expiry_date']]
    changed.columns=['CustomerID', 'FirstName', 'LastName', 'Email', 'Phone', 'Address',
       'CurrentFlag', 'Version', 'LoyaltyTier', 'PrevLoyaltyTier',
       'SubscriptionStart', 'SubscriptionEnd', 'expiry_date']
    df1=pd.concat([df1,changed], ignore_index=True)

    #SCD - 03

    merged=pd.merge(df1,df2,on='CustomerID',how='left',suffixes=('','_new'))

    j=merged.loc[((merged['LoyaltyTier']!=merged['LoyaltyTier_new']) & (merged['LoyaltyTier_new'].notnull()))]
    new=dict(zip(j['CustomerID'],j['LoyaltyTier_new']))
    old=dict(zip(j['CustomerID'],j['LoyaltyTier']))

    for i in new.keys():
        df1.loc[df1['CustomerID']==i,'LoyaltyTier']=new[i]

    for i in old.keys():
        df1.loc[df1['CustomerID']==i,'PrevLoyaltyTier']=old[i]

    #SCD - 04

    merged=pd.merge(df1,df2,on='CustomerID',how='left',suffixes=('','_new'))
    j=merged.loc[((merged['SubscriptionStart']!=merged['SubscriptionStart_new']) & (merged['SubscriptionStart_new'].notnull()))]
    df1.loc[df1['CustomerID'].isin(j['CustomerID']),'Version']+=1
    df1.set_index('CustomerID',inplace=True)
    df2.set_index('CustomerID',inplace=True)
    df1.update(df2['SubscriptionStart'])
    df1.reset_index(inplace=True)
    df2.reset_index(inplace=True)
    # print(df1)
    j=j.loc[:,j.columns.isin(df1.columns)]
    # print(j)
    # Insert new customers into the master table.
    existing_ids = df1['CustomerID'].unique()
    new_rows = df2[~df2['CustomerID'].isin(existing_ids)]
    new_rows['CurrentFlag']=1
    new_rows['Version']=1
    new_rows['PrevLoyaltyTier']=''
    df1=pd.concat([df1,new_rows], ignore_index=True)
    # print(df1)
    return df1,j

df1=pd.read_csv('Aug 25\\SCD_04\\src\\Customer_Master.csv')
df2=pd.read_csv('Aug 25\\SCD_04\\src\\Customer_Updates.csv')
transform_data(df1,df2)
