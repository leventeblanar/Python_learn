import pandas as pd

def calculate_discounted_price(df):
    df['discounted'] = df['price'] * df['discount']
    return df

def get_high_value_products(df):
    return df[df['discounted'] > 1000]

def main():
    data = {
        'product': ['TV', 'Phone', 'Laptop', 'Mouse'],
        'price': [500, 300, 1500, 80],
        'discount': [0.2, 0.15, 0.1, 0.5]  # percent-based discounts
    }

    df = pd.DataFrame(data)

    df = calculate_discounted_price(df)
    high_value_df = get_high_value_products(df)

    print("High value discounted products:")
    print(high_value_df)

if __name__ == '__main__':
    main()
