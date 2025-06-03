import requests
import base64
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_str = f"{client_id}:{client_secret}"
b64_auth_str = base64.b64encode(auth_str.encode()).decode()

token_url = "https://accounts.spotify.com/api/token"
headers = {
    "Authorization": f"Basic {b64_auth_str}"
}
data = {
    "grant_type": "client_credentials"
}

res = requests.post(token_url, headers=headers, data=data)

print("Status code:", res.status_code)
print("Raw response:", res.text)

try: 
    access_token = res.json()["access_token"]
    print("Token lekérdezve:", access_token)
except KeyError:
    print("Hiba: Nem találtam 'access tokent' a válaszban.")
