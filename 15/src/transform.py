import pandas as pd
import os

def transform():
    text={}
    for filename in os.listdir(r'Aug 22\15\src\resumes'):
        with open('Aug 22/15/src/resumes/'+filename,'r') as f:
            text[filename]=f.read()
    df=pd.DataFrame(columns=['name','phone','email','summary','experience'])
    for i in text.keys():
        line_text=text[i].split('\n')
        name=line_text[0].strip()
        text_ex=line_text[1].split('â™¦')
        phone=text_ex[1].strip()
        email=text_ex[2].strip()
        summary=(line_text[2]+line_text[3]+line_text[4]).lstrip('SUMMARY')
        experience=line_text[15]+','+line_text[21]
        new_row={'name':name,'phone':phone,'email':email,'summary':summary,'experience':experience}
        new_row=pd.DataFrame(new_row,index=[0])
        df=pd.concat([df,new_row])
    return df