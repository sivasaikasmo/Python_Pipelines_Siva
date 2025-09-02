# def load(df1,df2,engine):
#     df1.to_sql(name='project_details',con=engine,if_exists='replace',index=False)
#     df2.to_sql(name='project_technologies',con=engine,if_exists='replace',index=False)

#     return 'Loaded Succesfully'

from sqlalchemy import Table, Column,ForeignKey, MetaData, Text, DateTime,String

def load(df1,df2,engine):
    metadata = MetaData()

    project_details = Table('project_details', metadata,
    Column('project_id', String(50), primary_key=True),
    Column('project_name', Text()),
    Column('client', Text()),
    Column('domain', Text()),
    Column('location', Text()),
    Column('project_manager', Text()),
    Column('start_date', DateTime()),
    Column('end_date', DateTime()),
    Column('status', Text()),
    )

    project_technologies = Table('project_technologies', metadata,
    Column('project_id', String(50), ForeignKey('project_details.project_id')),
    Column('technologies', Text()))

    metadata.create_all(engine)
    
    connection=engine.connect()
    transaction=connection.begin()

    try:
        df1.to_sql(name='project_details',con=engine,if_exists='append',index=False)
        df2.to_sql(name='project_technologies',con=engine,if_exists='append',index=False)

        transaction.commit()
        return 'Loaded Succesfully'
    
    except Exception as e:
        transaction.rollback()
        return 'Transaction Failed'
    
    finally:
        connection.close()