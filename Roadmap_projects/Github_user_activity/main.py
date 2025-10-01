import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.github.com"
TOKEN = os.getenv("TOKEN")

headers = {"Authorization": "token {}".format(TOKEN)}


def get_user_activity(username):

    user_acitivty_endpoint = f"/users/{username}/events"
    get_user_activity_endpoint = BASE_URL + user_acitivty_endpoint

    try:
        response = requests.get(url=get_user_activity_endpoint, headers=headers, params={})
        resp_json = response.json()
        for event in resp_json:
            print(event["type"], "->", event["repo"]["name"])
    except Exception as e:
        print(f"Hiba történt a lekérdezés során {e}")


def main():

    username = str(input("Adj meg egy username-et, ahol látni szeretnéd az aktiviást: ")).strip().lower()
    lekeres = get_user_activity(username)
    

if __name__ == '__main__':
    main()
