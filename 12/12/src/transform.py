import pandas as pd

def transform(data):

    df_client=pd.json_normalize(data,
                         meta=['project_id','project_name',
                               ['client','name'],
                               ['client','industry'],
                               ['client','location','city'],
                               ['client','location','country'],
                               ['team','project_manager']
                         ])

    df_client.columns=['project_name','technologies','stack','milestones','project_id','client_name','client_industry','client_city','client_country'
                       ,'project_manager','team_members']
    # print(df_client)
    df_project=df_client[['project_id','project_name','stack','client_name','client_industry','client_city','client_country','project_manager']]

    # print(df_project)
    # # print(df_client['technologies'])

    df_technologies=df_client[['project_id','technologies']].explode('technologies')


    df_team_members=df_client[['project_id','team_members']].explode('team_members')
    # # print(df_team_members)
    
    df_team_members_1=pd.json_normalize(df_team_members['team_members'])

    # # print(df_team_members_1)

    df_team_members=df_team_members.reset_index(drop=True)

    df_team_members_1=df_team_members_1.reset_index(drop=True)

    df_team_members=pd.concat([df_team_members.drop(['team_members'],axis=1),df_team_members_1],axis=1)

    df_milestones=df_client[['project_id','milestones']].explode('milestones')

    df_milestones_1=pd.json_normalize(df_milestones['milestones'])

    df_milestones=df_milestones.reset_index(drop=True)
    df_milestones_1=df_milestones_1.reset_index(drop=True)
    df_milestones=pd.concat([df_milestones.drop(['milestones'],axis=1),df_milestones_1],axis=1)


    # # # Normalize data:
    # # #   Standardize project status (In Progress → Active, Planned → Pending, Completed → Done)
    # # #   Format city and country names consistently
    # # #   Convert milestone dates into DATE format
    # # # Clean & deduplicate data:
    # # #   Remove duplicates
    # # #   Handle missing or null values

    df_project['stack']=df_project['stack'].map({'In Progress':'Active','Planned':'Pending','Completed':'Done'})
    df_milestones['due_date']=pd.to_datetime(df_milestones['due_date'])

    return df_project,df_technologies,df_milestones,df_team_members
