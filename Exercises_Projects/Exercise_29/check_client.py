import pandas as pd
import json

def validate_partner(partner_dict):
    
    # This is to validate info on given partner

    ervenytelen_partnerek = []

    required_fields = ["name", "zip", "city", "address"]

    for partner in partner_dict:
        hibas = False
        print("-------------------")

        for field in required_fields:
            value = partner.get(field, "")
            print(f"{field.capitalize()}: {value}")
            if not value:
                print(f"Hiányzó {field} mező.")
                hibas = True
        
        if hibas:
            ervenytelen_partnerek.append(partner['name'])
        
    print("\nÉrvénytelen partnerek száma: ", len(ervenytelen_partnerek))
    print("\nÉrvénytelen partnerek: ", ervenytelen_partnerek)



with open('client_list.json', "r", encoding='utf-8') as file:
    partner_dict = json.load(file)

validate_partner(partner_dict)