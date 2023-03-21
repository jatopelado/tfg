import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import sys
from filesystem import filesystem

class gdrive(filesystem):
    def __init__(self):
        pass

    def archive(self,file_name):
    # Configurar las credenciales de OAuth 2.0
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json')
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret_479821468004-9ril7jibu39stovvn0ovp7gesdklgjk6.apps.googleusercontent.com.json', ['https://www.googleapis.com/auth/drive'])
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
    # Crear una instancia del cliente de la API de Google Drive
        service = build('drive', 'v3', credentials=creds)
    # Definir los parámetros del archivo que se subirá
        file_name = sys.argv[1]
        file_metadata = {'name': file_name}
        media = MediaFileUpload(file_name, resumable=True)
    # Subir el archivo a Google Drive
        file = service.files().create(body=file_metadata, media_body=media,
            fields='id').execute()
    # Obtener la URL pública del archivo
        file_id = file.get('id')
        permission = {'type': 'anyone', 'role': 'reader'}
        response = service.permissions().create(
        fileId=file_id, body=permission).execute()
        link = f'https://drive.google.com/uc?id={file_id}&export'
    # Imprimir la URL pública del archivo
        return(f'{link}')