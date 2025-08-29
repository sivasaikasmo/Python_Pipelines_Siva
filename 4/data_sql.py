#Load all provided datasets into SQL Server.

import pandas as pd
import pyodbc
import os


#Initial Loading data into sql server

df=pd.read_csv(r'D:\Kasmo\Python+Pyspark+Snowflake\Pipelines\2\order_data_1.csv')
df1=pd.read_csv(r'D:\Kasmo\Python+Pyspark+Snowflake\Pipelines\2\new_customerdata.csv')

conn=pyodbc.connect('DRIVER={SQL SERVER};SERVER=SSS-DESKTOP\\SQLEXPRESS;DATABASE=master;Trusted_Connection=yes;')


cursor=conn.cursor()

cursor.execute('create table order_data (order_id VARCHAR(100), '
    'customer_id INT, '
    'order_date DATE, '
    'order_amount FLOAT, '
    'order_status VARCHAR(10), '
    'product_category VARCHAR(100))'
)


cursor.execute('create table customer_data (customer_id int,' 
'name varchar(max),' 
'email varchar(max),' 
'phone varchar(max),' 
'address varchar(max),' 
'registration_date varchar(max),' 
'loyalty_status varchar(max))')


for index,row in df.iterrows():
    cursor.execute(
        "insert into order_data (order_id, customer_id, order_date, order_amount, order_status, product_category) values (?, ?, ?, ?, ?, ?)",
        row['order_id'], row['customer_id'], row['order_date'], row['order_amount'], row['order_status'], row['product_category'])

for index, row in df1.iterrows():
    values = [x if pd.notna(x) else None for x in row]
    try:
        cursor.execute(
            "insert into customer_data (customer_id, name, email, phone, address, registration_date, loyalty_status) values (?, ?, ?, ?, ?, ?, ?)",
            values[1],values[2],values[3],values[4],values[5],values[6],values[7]
        )
    except Exception as e:
        print(row)
        print(e)

conn.commit()
cursor.close()
conn.close()

