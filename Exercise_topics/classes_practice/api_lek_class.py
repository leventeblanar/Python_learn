import requests

class User:
    def __init__(self, name, username, email, city, website):
        self.name = name
        self.username = username
        self.email = email
        self.city = city
        self.website = website

    @classmethod
    def from_json(cls, data):
        name = data.get("name", "")
        username = data.get("username", "")
        email = data.get("email", "")
        city = data.get("city", "")
        website = data.get("website", "")
        return cls(name, username, email, city, website)
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Username: {self.username}")
        print(f"City: {self.city}")
        print(f"Email: {self.email}")
        print(f"Website: {self.website}")
        print(f"_" * 40)
        
def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    if response.status_code == 200:
        users_data = response.json()
        print(users_data)
        return [User.from_json(user) for user in users_data]
    else: 
        print("Hiba történt az adatok lekérésekor.")
        return []
    
if __name__ == "__main__":
    users = fetch_users()
    
    for user in users:
        user.display_info()