import pandas as pd

def reading_csv():

    drinks_df = pd.read_csv('pandas_csv/drinks.csv')
    return drinks_df


def no_beer():

    drinks_df = reading_csv()

    no_beers_df = drinks_df[drinks_df["beer_servings"] == 0]
    no_beers_df.to_csv("no_beer.csv", index=False)


def beer_more_300():

    drinks_df = reading_csv()

    beers_df = drinks_df[drinks_df["beer_servings"] > 300]
    beers_df.to_csv("beers_300.csv", index=False)

def complex_sort_beer_wine():

    drinks_df = reading_csv()

    sort_df = drinks_df[(drinks_df["wine_servings"] >= 100) & (drinks_df["beer_servings"] < 50)]
    sort_df.to_csv('complex_sort.csv') 



def new_column():

    drinks_df = reading_csv()

    drinks_df["high_alcohol"] = drinks_df["total_litres_of_pure_alcohol"] >= 10
    only_high_alcohol = drinks_df[drinks_df["high_alcohol"] == True]

    only_high_alcohol.to_csv("only_high_alcohol.csv")


def new_column_v2():

    drinks_df = reading_csv()

    