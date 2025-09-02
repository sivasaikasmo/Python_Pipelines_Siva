# Flatten the data to extract all relevant fields:
#   project_id, project_name, client, domain, location, project_manager, start_date, end_date, status
# Explode the technologies array into a separate table.
# Normalize project status:
#   "In Progress" → "Active"
#   "Planned" → "Pending"
#   "Completed" → "Done"
# Convert dates (start_date, end_date) into proper DATE format.
# Clean data:
#   Remove duplicates
#   Ensure all mandatory fields are populated
# Optionally, capitalize location and domain names for consistency.

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




