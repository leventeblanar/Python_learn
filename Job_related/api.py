import requests

def get_api_response():

    url="https://pokeapi.co/api/v2/pokemon/pikachu"
    res = requests.get(url)
    data = res.json()

    print("Név: ", data["name"])
    print("Magasság:", data["height"])
    print("Típusok: ")
    for t in data["types"]:
        print("-", t["type"]["name"])



class Pokemon:

    def __init__(self, name):
        self.name = name


    def get_data_from_api(self):

        url = f"https://pokeapi.co/api/v2/pokemon/{self.name}"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
        else:
            print(f"Hiba: {res.status_code} - Válasz: {res.text}")

        print("Név: ", data["name"])
        print("Magasság: ", data["height"])
        print("Típusok: ")
        for t in data["types"]:
            print("-", t["type"]["name"])


# pokemon1 = Pokemon("pikachu")
# pokemon1.get_data_from_api()

# pokemon2 = Pokemon("squirtle")
# pokemon2.get_data_from_api()

# pokemon3 = Pokemon("Lajos")
# pokemon3.get_data_from_api()