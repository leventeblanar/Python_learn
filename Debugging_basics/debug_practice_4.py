import pandas as pd

def clean_prices(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    return df

def apply_discounts(df):
    df['final_price'] = df['price'] * (1 - df['discount'])
    return df

def categorize_products(df):
    conditions = [
        df['final_price'] > 1000,
        df['final_price'] > 500
    ]
    choices = ['High-end', 'Mid-range']
    df['category'] = pd.Series(pd.cut(df['final_price'], bins=[0, 500, 1000, float('inf')], labels=['Low', 'Mid', 'High']))
    return df

def filter_valid_rows(df):
    return df.dropna(subset=['price', 'discount', 'final_price'])

def main():
    data = {
        'product': ['TV', 'Laptop', 'Phone', 'Mouse', 'Fridge'],
        'price': ['500', '1500', 'abc', '80', '1200'],
        'discount': [0.1, 0.2, 0.05, 0.5, None]
    }

    df = pd.DataFrame(data)

    df = clean_prices(df)
    df = apply_discounts(df)
    df = filter_valid_rows(df)
    df = categorize_products(df)

    print("Final processed products:")
    print(df[['product', 'final_price', 'category']])

if __name__ == '__main__':
    main()
