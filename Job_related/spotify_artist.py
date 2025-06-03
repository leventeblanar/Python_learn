import os
import base64
import requests
from dotenv import load_dotenv


# API connections always require
# - a url
# - header info (token)
# - params if get, payload if post, pull

class SpotifyClient:
    def __init__(self):
        load_dotenv()
        # cliet_id and client_secret comes from .env
        self.client_id = os.getenv("SPOTIFY_CLIENT_ID").strip()
        self.client_secret = os.getenv("SPOTIFY_CLIENT_SECRET").strip()
        # token comes from the get_token method
        self.token = self.get_token()
        # headers comes from the token information()
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_token(self):
        # authorization string is consturcted from the client id and secret
        auth_str = f"{self.client_id}:{self.client_secret}"
        b64_auth_str = base64.b64encode(auth_str.encode()).decode()

        # we have to get a token from the below link
        url = "https://accounts.spotify.com/api/token"


        headers = {
            "Authorization": f"Basic {b64_auth_str}"
        }
        data = {
            "grant_type": "client_credentials"
        }

        # the post methods parameter is the url, the headers (this has the decoded client_id and client secret and the data)
        res = requests.post(url, headers=headers, data=data)
        if res.status_code != 200:
            raise Exception(f"Hiba a token lekéréskor: {res.text}")
        # return only the access token from the json response from the page
        return res.json()["access_token"]
    
    def search_artist(self, artist_name):

        url = "https://api.spotify.com/v1/search"
        params = {
            "q": artist_name,
            "type": "artist",
            "limit": 1
        }

        res = requests.get(url, headers=self.headers, params=params)
        # we only need the artist name and the items 
        results = res.json()["artists"]["items"]
        if not results:
            print(f"Nem található előadó: {artist_name}")
            return None
        # and return only the 1 find's id - this will be used for searching top tracks from given artist as I assume that tracks only have artist id
        return results[0]["id"]
    
    def get_top_tracks(self, artist_id, country="USA"):
        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
        params = {"country": country}
        res = requests.get(url, headers=self.headers, params=params)
        return res.json()["tracks"]
    
    def print_top_tracks(self, artist_name, limit=5):
        artist_id = self.search_artist(artist_name)
        if not artist_id:
            return
        tracks = self.get_top_tracks(artist_id)
        print(f"\n {artist_name.title()} legnépszerűbb számai:\n")
        for i, track in enumerate(tracks[:limit], start=1):
            print(f"{i}. {track['name']} ({track['external_urls']['spotify']})")


spotify = SpotifyClient()
spotify.print_top_tracks('metallica')