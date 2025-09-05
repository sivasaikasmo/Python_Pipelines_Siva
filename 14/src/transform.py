import pandas as pd
import re

def clean_text(text):
    text=re.sub(r"http\S+","",text)
    text = re.sub(r"@\w+", "", text)            
    text = re.sub(r"#\w+", "", text)            
    text = re.sub(r"[^\w\s]", "", text) 
    return text.strip()

def transform(data):
    df=pd.json_normalize(data)
    df=df[['id','created_at','text','author_id','public_metrics.retweet_count','public_metrics.like_count']]
    df['clean_text']=df['text'].apply(clean_text)
    df=df.drop_duplicates(subset=['id'])
    df=df.drop(columns=['text'])
    df=df.reset_index(drop=True)
    df['created_at']=pd.to_datetime(df['created_at']).dt.date
    return df
    
