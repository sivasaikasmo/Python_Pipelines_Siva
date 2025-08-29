# Identify New vs Existing Customers (Mapping)
# Compare extracted customers with existing dimension table (dim_customers).
# Match on customer_id.
# Detect Attribute Changes
# If any of region, loyalty_tier, email changed → mark as changed record.
# Expire Old Record
# For changed records:
# Set valid_to = current_date - 1
# Set is_current = 'N'.
# Insert New Record Version
# Insert a new row for the changed customer with:
# valid_from = current_date
# valid_to = '9999-12-31'
# is_current = 'Y'.
# Handle New Customers
# If customer_id not found in dimension table → insert as new record (first version).
# Preserve History
# Maintain all past versions for each customer_id.
# Optional Enrichment (Mapping)
# Add audit columns: record_source, etl_batch_id, last_updated_by.

import pandas as pd 
from datetime import datetime

def transform_data(df1,df2):
    merged=pd.merge(df1,df2,on='customer_id',how='left',suffixes=('','_new'))
    chng_dct=[]
    for i in ['name','region','loyalty_tier','email']:
        j=merged.loc[((merged[i]!=merged[i+'_new']) & (merged[i+'_new'].notnull()))]
        chng_dct.extend(j['customer_id'].to_list())
    now=pd.to_datetime(datetime.now())-pd.Timedelta(days=1)
    print(now.date())
    df1.loc[df1['customer_id'].isin(chng_dct),['valid_to', 'is_current']] = [now.date(), 'N']
    new_dat=df2.loc[df2['customer_id'].isin(chng_dct)]
    # print(chng_dct)
    # print(df1)
    new_dat['valid_to']='9999-12-31'
    new_dat['is_current']='Y'
    df1=df1.drop(columns=['index'])
    # print(new_dat)
    new_dat.columns=['surrogate_key','customer_id','name','region','loyalty_tier','email','valid_from','valid_to','is_current']
    df1=pd.concat([df1,new_dat])
    existing_ids = df1['customer_id'].unique()
    new_rows = df2[~df2['customer_id'].isin(existing_ids)]
    # print(new_rows)
    # new_rows['CurrentFlag']=1
    # new_rows['Version']=1
    # new_rows['PrevLoyaltyTier']=''
    # new_rows['expiry_date']=''
    # df1=pd.concat([df1,new_rows], ignore_index=True)
    return df1




