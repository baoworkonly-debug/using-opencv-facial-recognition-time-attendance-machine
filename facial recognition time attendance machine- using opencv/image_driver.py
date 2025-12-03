from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import requests
import json, os
import datetime



def img(time_str):


    

    #file_name = f'{time_str}.jpeg'

    #output_dir = 'D:\CODEEEEE\cham_cong\check_in'
    #file_name = os.path.join(output_dir, f"face_{time_str}.jpeg")

    CLIENT_SECRE_FILE = 'client_secret.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']
    service =  Create_Service(CLIENT_SECRE_FILE, API_NAME, API_VERSION, SCOPES)

    folder_id = '15m2S1ZOxfQgQZ11sVlUpB-LlcBtii4Lf'
    file_type = 'image/jpeg'
    file_metadata = {
        'name': time_str,
        'parents': [folder_id]
    }
    media = MediaFileUpload(file_name, mimetype=file_type)
    service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'

        ).execute()
   
 