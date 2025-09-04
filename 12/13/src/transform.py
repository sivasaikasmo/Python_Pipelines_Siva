import pandas as pd


def transform(data):
    df_client=pd.json_normalize(data)
    df_technologies=df_client[['project_id','technologies']].explode('technologies')
    df_client=df_client.drop(['technologies'],axis=1)
    df_client['status']=df_client['status'].map({"In Progress":"Active","Planned":"Pending","Completed":"Done"})
    df_client['start_date']=pd.to_datetime(df_client['start_date'])
    df_client['end_date']=pd.to_datetime(df_client['end_date'])
    df_client['location']=df_client['location'].str.upper()
    df_client['domain']=df_client['domain'].str.upper()
    
    return df_client,df_technologies