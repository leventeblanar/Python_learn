
import pandas as pd


# lambda - egysoros, névtelen függvény, olyan mintha gyorsan akarnál írni egy def nélküli függvényt,
# amit mondjuk csak egy list() vagy sorted() vagy map() belsejében használsz

def basics():
    add_2 = lambda x: x + 2
    print(add_2(4))

    multiply_5 = lambda x: x * 5
    print(multiply_5(4))


    triple = lambda x: x * 3
    print(triple(6))


    add_numbers = lambda a, b: a + b
    print(add_numbers(5, 9))


    is_even = lambda x: x % 2 == 0
    print(is_even(4))
    print(is_even(7))


    numbers_double = [1, 2, 3, 4]
    doubled = list(map(lambda x: x * 2, numbers_double))
    print(doubled)

    numbers_square = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers_square))
    print(squared)


    words = ["apple", "banana", "kiwi", "pear"]
    count_letters = list(map(lambda x: len(x), words))
    print(count_letters)


    weights = [20, 30, 50]

    add_kg = list(map(lambda x: str(x) + "kg", weights))
    print(add_kg)


    names = ['Anna', 'Béla', 'Cecil', 'Lajos']

    remove_1st = list(map(lambda name: name[0], names))
    print(remove_1st)


    net_prices = [100, 250, 430]

    brutto = list(map(lambda x: round(x * 1.27, 1), net_prices))
    print(brutto)


    words = ['körte', 'alma', 'szilva', 'a']
    sort_by_len = sorted(words, key=lambda x: len(x))
    print(sort_by_len)


def lambda_dataframe():

    only_hight_alcohol_df = pd.read_csv('only_high_alcohol.csv')
    
    # addig a column of below 12l of alc
    only_hight_alcohol_df['below_12l'] = only_hight_alcohol_df['total_litres_of_pure_alcohol'].apply(lambda x: x < 12)

    only_hight_alcohol_df['double'] = only_hight_alcohol_df.apply(lambda row: row['total_litres_of_pure_alcohol'] * 2, axis=1)

    print(only_hight_alcohol_df)


def beer_percentage():

    df = pd.read_csv('only_high_alcohol.csv', sep=",")

    df['beer_percentage'] = df.apply(lambda row: row['beer_servings'] / (row['beer_servings'] + row['spirit_servings'] + row['wine_servings']) * 100, axis=1)

    df.to_csv('df_check.csv')


def wine_countries():

    df = pd.read_csv('only_high_alcohol.csv', sep=",")

    df['wine_dominant'] = df['wine_servings'].apply(lambda x: x > 250)

    print(df)


def which_drink():

    df = pd.read_csv('only_high_alcohol.csv', sep=",")
    
    df['top_drink'] = df.apply(
        lambda row: max(
            {'beer': row['beer_servings'],
             'wine': row['wine_servings'],
             'spirit': row['spirit_servings']},
            key=lambda k: row[k + '_servings']
        ),
        axis=1
    )

    return df


def alcohol_category():

    df = pd.read_csv('only_high_alcohol.csv', sep=",")
    
    df['alcohol_level'] = df['total_litres_of_pure_alcohol'].apply(
        lambda x: 'low' if x<10 else ('medium' if x<=12 else 'high')
    )

    print(df)


def alcohol_warning():

    df = pd.read_csv('only_high_alcohol.csv', sep=",")

    df['alcohol warning'] = df['total_litres_of_pure_alcohol'].apply(
        lambda x: 'none' if x < 10 else ('watch_out' if x<=12 else 'danger')
    )

    print(df)


def wine_or_beer():

    df = pd.read_csv('only_high_alcohol.csv', sep=",")
    
    df['preference'] = df.apply(
        lambda row: 'beer' if row['beer_servings'] > row['wine_servings'] else 'wine', axis=1
    )

    print(df)

def drink_tip():

    top_drink = which_drink()

    top_drink['drink_tip'] = top_drink['top_drink'].apply(
        lambda x: 'Try a local beer' if x == 'beer'
        else ('Try a local wine' if x == 'wine' else 'spirit')
    )

    print(top_drink)

basics()