import pandas as pd
from datetime import datetime

def transform(df1,df2):
    merged=pd.merge(df1,df2,on='CustomerID',how='left',suffixes=('','_new'))
    changed=merged.loc[((merged['FirstName']!=merged['FirstName_new']) & (merged['FirstName_new'].notnull())) | \
                ((merged['LastName']!=merged['LastName_new']) & (merged['LastName_new'].notnull())) | \
                ((merged['Email']!=merged['Email_new']) & (merged['Email_new'].notnull())) | \
                ((merged['Phone']!=merged['Phone_new']) & (merged['Phone_new'].notnull())) | \
                ((merged['Address']!=merged['Address_new']) & (merged['Address_new'].notnull())) | \
                ((merged['LoyaltyTier']!=merged['LoyaltyTier_new']) & (merged['LoyaltyTier_new'].notnull())) | \
                ((merged['SubscriptionStart']!=merged['SubscriptionStart_new']) & (merged['SubscriptionStart_new'].notnull())) | \
                ((merged['SubscriptionEnd']!=merged['SubscriptionEnd_new']) & (merged['SubscriptionEnd_new'].notnull()))  ]
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
    existing_ids = df1['CustomerID'].unique()
    new_rows = df2[~df2['CustomerID'].isin(existing_ids)]
    new_rows['CurrentFlag']=1
    new_rows['Version']=1
    new_rows['PrevLoyaltyTier']=''
    new_rows['expiry_date']=''
    df1=pd.concat([df1,new_rows], ignore_index=True)
    df1=df1.drop('PrevLoyaltyTier',axis=1)

    return df1






