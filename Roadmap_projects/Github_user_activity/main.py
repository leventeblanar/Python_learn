import requests
import json
import os, sys
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.github.com"
TOKEN = os.getenv("TOKEN")
HEADERS = {"Authorization": f"token {TOKEN}"} if TOKEN else {}


def get_user_events(username: str):
    url = f"{BASE_URL}/users/{username}/events"
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()

def print_events(events):
    for e in events:
        etype = e.get("type", "?")
        repo = e.get("repo", {}).get("name", "?")
        line = f"{etype} -> {repo}" 
        if etype == "PushEvent":
            commits = e.get("payload", {}).get("commits", [])
            if commits:
                msgs = " | ".join(c.get("message", "") for c in commits if c)
                line += f" -> {msgs}"
        print(line)


def main():

    username = sys.argv[1] if len(sys.argv) > 1 else input("GitHub username: ").strip()
    events = get_user_events(username)
    print_events(events)
    

if __name__ == '__main__':
    main()
