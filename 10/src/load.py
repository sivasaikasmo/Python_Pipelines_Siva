def load(df1,df2,df3,df4,engine):
    df1.to_sql(name='projects',con=engine,if_exists='replace',index=False)
    df2.to_sql(name='project_technologies',con=engine,if_exists='replace',index=False)
    df4.to_sql(name='project_team_members',con=engine,if_exists='replace',index=False)
    df3.to_sql(name='project_milestones',con=engine,if_exists='replace',index=False)

    return 'Loaded Succesfully'