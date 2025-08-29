import pandas as pd

def transform_data(df1,df2):
    merged=pd.merge(df1,df2,on='CustomerID',how='left',suffixes=('','_new'))
    chng_dct={}
    chng_dct_old={}
    for i in ['FirstName','LastName','Email','Phone','Address','LoyaltyTier']:
        j=merged.loc[((merged[i]!=merged[i+'_new']) & (merged[i+'_new'].notnull()))]
        new=dict(zip(j['CustomerID'],j[i+'_new']))
        old=dict(zip(j['CustomerID'],j[i]))
        chng_dct_old[i]=old
        chng_dct[i]=new
    df1['prevFristName']=''
    df1['prevLastName']=''
    df1['prevEmail']=''
    df1['prevPhone']=''
    df1['prevAddress']=''
    for i in chng_dct.keys():
        for j in chng_dct[i]:
            df1.loc[df1['CustomerID']==j,i]=chng_dct[i][j]
    
    for i in chng_dct_old.keys():
        for j in chng_dct_old[i]:
            df1.loc[df1['CustomerID']==j,'prev'+i]=chng_dct_old[i][j]

    df1=df1.drop(['prevFristName','prevLastName','PrevLoyaltyTier'],axis=1)

    existing_ids = df1['CustomerID'].unique()
    new_rows = df2[~df2['CustomerID'].isin(existing_ids)]
    new_rows['CurrentFlag']=1
    new_rows['Version']=1
    # print(new_rows)

    df1=pd.concat([df1,new_rows],ignore_index=True)
    # print(df1)
    # print(df1.columns)
    return df1

