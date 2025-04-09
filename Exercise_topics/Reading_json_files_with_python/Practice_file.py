import pandas as pd
import json

def dict_to_json():

    x = {
    "name": "John",
    "age": 30,
    "city": "New York"
    }

    convert_to_json = json.dumps(x)

    print(convert_to_json)

def beolvasás_1():

    with open('src/country-by-capital-city.json') as country_capital:
        capitals = json.load(country_capital)

    with open('src/country-by-currency-name.json') as currency:
        currency_data = json.load(currency)

    cities_in_json = []

    for item in capitals:
        city = item.get("city")
        cities_in_json.append(city)

    for city in cities_in_json:
        char_count = len(str(city))
        if char_count > 8:
            print(f"This is a long city name: {city}")
        else:
            print(f"This is not a long city name: {city}")


def join_json():
    
    capital_df = pd.read_json('src/country-by-capital-city.json')
    currency_df = pd.read_json('src/country-by-currency-name.json')
    government_df = pd.read_json('src/country-by-government-type.json')

    merged_df  = capital_df.merge(currency_df, on="country", how="left")
    add_governemnt_df = merged_df.merge(government_df, on="country", how="left")
    add_governemnt_df = add_governemnt_df.fillna("")

    combined_data = add_governemnt_df.to_dict(orient="records")

    with open("export/final_json.json", "w", encoding="utf-8") as f:
        json.dump(combined_data, f, indent=4, ensure_ascii=False)

def join_without_dataframe():

    # open json with capital cities
    with open('src/country-by-capital-city.json') as country_capital:
        capitals = json.load(country_capital)
    # open json with currency
    with open('src/country-by-currency-name.json') as currency:
        currency_data = json.load(currency)

    # capital dictionary = 
    capital_dict = {item['country']: item.get('city', '') for item in capitals}

    combined_data = []

    for item in currency_data:
        country = item.get('country')
        currency = item.get('currency_name')

        city = capital_dict.get(country, '')

        combined_data.append({
            "country": country,
            "currentcy_name": currency,
            "city": city
        })

        with open('export/combined.json', 'w', encoding='utf-8') as f_out:
            json.dump(combined_data, f_out, indent=4, ensure_ascii=False)

def join_json_to_json():

    with open('export/combined_json.json') as combined:
        combined_json = json.load(combined)

    with open('src/country-by-elevation.json') as elevation:
        elevation_json = json.load(elevation)

    elevation_dict = {item['country']: item.get('elevation', '') for item in elevation_json}

    combined_data2 = []

    for item in combined_json:
        country = item.get('country')
        city = item.get('city')
        currency_name = item.get('currency_name')

        elevation = elevation_dict.get(country, '')

        combined_data2.append({
            "country": country,
            "currency_name": currency_name,
            "city": city,
            "elevation": elevation
        })

        with open('export/combined2_json.json', 'w', encoding='utf-8') as f_out:
            json.dump(combined_data2, f_out, indent=4, ensure_ascii=False)

    print('Json exportálva.')        

def join_governement_to_combined2():

    with open('export/combined2_json.json', 'r', encoding='utf-8') as combined:
        combined_json = json.load(combined)

    with open('src/country-by-government-type.json', 'r', encoding='utf-8') as government:
        government_json = json.load(government)

    government_dict = {item['country']: item.get('government', '') for item in government_json}

    combined_data3 = []

    for item in combined_json:
        country = item.get('country')
        city = item.get('city')
        currency_name = item.get('currency_name')
        elevation = item.get('elevation')

        government = government_dict.get(country, '')

        combined_data3.append({
            'country': country,
            'city': city,
            'currency_name': currency_name,
            'elevation': elevation,
            'government': government
        })

        with open('export/combined3_json.json', 'w', encoding='utf-8') as f_out:
            json.dump(combined_data3, f_out, indent=4, ensure_ascii=False)

        print('json')


def join_national_dishtocombined3():

    with open('src/country-by-national-dish.json', encoding='utf-8') as natdish:
        natdish_json = json.load(natdish)

    with open('export/combined3_json.json', encoding='utf-8') as combined3:
        combined3_json = json.load(combined3)

    natdish_dict = {item['country']: item.get('dish', '') for item in natdish_json}

    combined_data4 = []

    for item in combined3_json:
        country = item.get('country')
        city = item.get('city')
        currency_name = item.get('currency_name')
        elevation = item.get('elevation')
        government = item.get('government')

        nat_dish = natdish_dict.get(country, '')

        combined_data4.append({
            'country': country,
            'city': city,
            'currency_name': currency_name,
            'elevation': elevation,
            'government': government,
            'national_dish': nat_dish
        })

        with open('export/combined4_json.json', 'w', encoding='utf-8') as f_out:
            json.dump(combined_data4, f_out, indent=4, ensure_ascii=False)

def join_national_dishtocombined4():

    with open('src/country-by-independence-date.json', encoding='utf-8') as independence:
        independence_json = json.load(independence)

    with open('export/combined4_json.json', encoding='utf-8') as combined4:
        combined4_json = json.load(combined4)

    independence_dict = {item['country']: item.get('independence', '') for item in independence_json}

    combined_data5 = []

    for item in combined4_json:
        country = item.get('country')
        city = item.get('city')
        currency_name = item.get('currency')
        elevation = item.get('elevation')
        government = item.get('government')
        national_dish = item.get('national_dish')

        independence = independence_dict.get(country, '')

        combined_data5.append({
            'country': country,
            'city': city,
            'currency_name': currency_name,
            'elevation': elevation,
            'government': government,
            'national_dish': national_dish,
            'independence': independence
        })
    
    with open('export/combined5_json.json', 'w', encoding='utf-8') as f_out:
        json.dump(combined_data5, f_out, indent=4, ensure_ascii=False)


def format_to_Dataframe():

    with open('export/combined4_json.json', encoding='utf-8') as combined4:
        combined4_json = json.load(combined4)

    combined_df = pd.DataFrame(combined4_json, columns=['country', 'city', 'currency_name', 'elevation', 'government', 'national_dish'])
    combined_df.columns = ['country', 'city', 'currency_name', 'elevation', 'government', 'national_dish']

    print(combined_df.head(10))

if __name__ == '__main__':
    join_national_dishtocombined4()