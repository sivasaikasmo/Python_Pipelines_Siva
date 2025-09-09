import os
import io
import pdfplumber

def extract(session):
    s3=session.client('s3')
    response=s3.list_objects_v2(Bucket='resume-etl')
    keys=[]
    for obj in response.get('Contents',[]):
        if not obj['Key'].startswith('archive/'):
            keys.append(obj['Key'])
    for i in keys:
        all_text=''
        response=s3.get_object(Bucket='resume-etl',Key=i)
        file_stream=io.BytesIO(response['Body'].read())
        with pdfplumber.open(file_stream) as pdf:
            for page in pdf.pages:
                text=page.extract_text()
                if text:
                    all_text+=text+"\n"
            file_path=os.path.join(r'D:\Kasmo\Python+Pyspark+Snowflake\Pipelines\Aug 22\15\src\resumes',i[0:i.find('.')]+'.txt')
            with open(file_path,'w',encoding='utf-8') as f:
                f.write(all_text)
        s3.copy_object(Bucket='resume-etl',CopySource={'Bucket': 'resume-etl', 'Key': i},Key='archive/'+i)
        s3.delete_object(Bucket='resume-etl',Key=i)
            
    return 'Text Extracted'
