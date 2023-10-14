# エンドユーザーとして認証する場合のコード
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

json_file = "secret.json"

appflow = InstalledAppFlow.from_client_secrets_file(
    json_file,
    scopes=['https://www.googleapis.com/auth/drive.file']
)

launch_browser = True

if launch_browser:
    appflow.run_local_server()
else:
    appflow.run_console()

credentials = appflow.credentials
