import pandas as pd


def extract(session):
    
    dynamodb = session.resource("dynamodb")
    table=dynamodb.Table('projects_json')

    response=table.scan()
    items=response["Items"]

    return items
