import pandas as pd

def normalize_prices(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['price'] = df['price'] / 100
    return df

def filter_products(df):
    filtered = df[df['price'] > 1.00]
    return filtered

def main():
    data = {
        'product': ['Milk', 'Bread', 'Eggs', 'Caviar'],
        'price': ['250', 'abc', '300', '1200']
    }

    df = pd.DataFrame(data)

    df = normalize_prices(df)
    df = filter_products(df)

    print("Filtered products:")
    print(df)

if __name__ == '__main__':
    main()
