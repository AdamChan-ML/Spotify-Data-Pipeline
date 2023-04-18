import os
import requests
import json
import base64
from dotenv import load_dotenv

load_dotenv()

refresh_token = os.getenv("REFRESH_TOKEN")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
client_creds = f"{client_id}:{client_secret}"

# Converting client_creds into base64 format
base64_bytes = base64.b64encode(client_creds.encode('ascii'))
base_64_client_creds = base64_bytes.decode('ascii')

class Refresh:

    def __init__(self):
        self.refresh_token = refresh_token
        self.base_64_client_creds = base_64_client_creds

    def refresh(self):

        query = "https://accounts.spotify.com/api/token"

        response = requests.post(query,
                                 data={"grant_type": "refresh_token",
                                       "refresh_token": refresh_token},
                                 headers={"Authorization": "Basic " + base_64_client_creds})

        response_json = response.json()

        return response_json["access_token"]