import os
import requests
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
auth_code = os.getenv('AUTH_CODE')

# Ensure that authorization code has been set in dot env file before running this function
def get_token():
    url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'code': auth_code,
        'redirect_uri': "http://localhost:8888/callback"
    }
    token = requests.post(url, data=data)
    token = token.json()
    print(token)
    return token['access_token']

get_token()