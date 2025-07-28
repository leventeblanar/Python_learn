import pandas as pd

def filter_data(df):
    df['price'] = df['price'].astype(float)
    filtered = df[df['price'] > 100]
    return filtered

def calc_average_price(df):
    total = 0
    for price in df['price']:
        total += price
    avg = total / len(df['price'])
    return round(avg, 2)

data = {
    'product': ['A', 'B', 'C', 'D'],
    'price': ['120.5', 'abc', '99.9', '150']
}

df = pd.DataFrame(data)

filtered_df = filter_data(df)
avg_price = calc_average_price(filtered_df)

print("Átlagár (100 felett):", avg_price)
