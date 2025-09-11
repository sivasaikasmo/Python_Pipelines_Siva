from __future__ import annotations
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import io
import numpy as np

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

def transform(session,response,service):

    s3=session.client('s3')
    mails=[]


    for msg in response.get('messages',[]):
        msg_id = msg['id']
        full_msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
        payload = full_msg.get('payload', {})
        headers = payload.get('headers', [])
        def get_header(name):
            return next((h['value'] for h in headers if h['name'].lower() == name.lower()), None)

        sender = get_header('From')
        receiver = get_header('To')
        cc = get_header('Cc')
        subject = get_header('Subject')
        date = get_header('Date')

        # for subpart in payload.get('parts',[]):
        #     if subpart.get('mimeType') in ['text/plain','text/html']:
        #         body=subpart.get('body',{})
        #         data=body.get('data')
        #         body_text=base64.urlsafe_b64decode(data).decode('utf-8', errors='replace')

        # print(body_text)
        attachments=[]

        for subpart in payload.get('parts',[]):
            filename=subpart.get('filename')
            if filename:
                att_id=subpart['body'].get('attachmentId')
                if att_id:
                    att=service.users().messages().attachments().get(userId='me',messageId=msg_id,id=att_id).execute()
                    file_data=base64.urlsafe_b64decode(att['data'])
                    file_obj=io.BytesIO(file_data)
                    s3.upload_fileobj(file_obj,'gmail-att',filename)
                    url=f"https://gmail-att.s3.us-east-1.amazonaws.com/{filename}"
                    attachments.append(url)
        
        # print(attachments)

        data={"msg_id":msg_id,"sender":sender,"receiver":receiver,"cc":cc,"subject":subject,"date":date}
        if len(attachments)>0:
            data['attachment_1']=attachments[0]
        else:
            data['attachment_1']=np.nan
        if len(attachments)>1:
            data['attachment_2']=attachments[1]
        else:
            data['attachment_2']=np.nan

        mails.append(data)

    return mails
    