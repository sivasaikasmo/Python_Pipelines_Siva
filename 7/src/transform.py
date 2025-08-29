# Transformations (8–10 steps)
# 1.Join Orders + Order Items
# Create line-level sales data.
# 2.Compute Line Total
# line_total = quantity * price.
# 3.Filter Only Completed Orders
# Keep only status = 'COMPLETE'.
# 4.Add Discount Column (Business Rule)
# Example: If quantity ≥ 5, apply 10% discount.
# net_total = line_total - (discount).
# 5.Derive Order Month & Year (Date Transformation)
# Extract month and year from order_date for trend analysis.
# 6.Aggregate at Order Level
# Compute:
# order_total (sum of line totals)
# total_quantity
# 7.Customer Region Join
# Attach region from customers for regional breakdown.
# 8.Sales by Region + Month (Aggregation)
# GROUP BY region, year, month → total revenue, order count.

# 9.Category-wise Analysis (Enrichment)
# Join products → compute sales by category.
# 10.Ranking Transformation
# Add region_rank by revenue → helps find top-performing regions.
# 11.Sorting
# Sort by year, month, total_revenue DESC.
# 12.Outlier Flagging (Optional)
# Flag orders where order_total > 95th percentile.

import pandas as pd

def transform(df1,df2,df3,df4):
    df3=df3.merge(df2,on='order_id',how='left')
    df3['total']=df3['quantity']*df3['price']
    df3=df3.loc[df3['status']=='COMPLETE']
    df3['net_total']=df3.apply(lambda x: x['total']-x['total']*0.1 if x['quantity']>=5 else x['total'],axis=1)
    df3['month']=pd.to_datetime(df3['order_date']).dt.month
    df3['year']=pd.to_datetime(df3['order_date']).dt.year
    df3=df3.groupby(['order_id','customer_id','order_date','product_id','month','year']).agg({'quantity':'sum','net_total':'sum'})
    df3=df3.reset_index()
    df3=df3.merge(df1,on='customer_id',how='left')
    df3=df3.groupby(['region','year','month','product_id']).agg({'order_id':'count','net_total':'sum'})
    df3=df3.reset_index()
    df3.columns=['region','year','month','product_id','orders','total']
    df3=df3.merge(df4,on='product_id',how='left')
    df3=df3.groupby(['region','year','month','category']).agg({'total':'sum'})
    df3=df3.reset_index()
    df3['region_category_rank'] = df3.groupby('region')['total'].rank(ascending=False)
    df3=df3.sort_values(by=['year','month','total'],ascending=[False,False,False])
    threshold = df3['total'].quantile(0.95)
    df3['high_order_flag']=df3['total']>threshold
    return df3





