import pandas as pd
import json

with open('client_list.json', "r", encoding='utf-8') as file:
    partner_dict = json.load(file)

print(partner_dict)

def validate_partner():
    pass