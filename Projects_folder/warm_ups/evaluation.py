

def parse_product(row):
    if row == "":
        return None, {
            "row": row,
            "reason": "Üres sor"
        }
    
    try:
        product, amount, price = row.split(";")
    except ValueError:
        return None, {
            "row": row,
            "reason": "Nem megfelelő formétum. Elvárt: name; quantity; unit_price;"
        }
    
    product_name = product.strip()
    if product_name == "":
        return None, {
            "row": row,
            "reason": "Hiányzó terméknév"
        }
    
    try:
        product_amount = int(amount)
        product_price = int(price)
    except ValueError:
        return None, {
            "row": row,
            "reason": "A darabszám vagy az ár nem alakítható számmá."
        }


    if product_amount <= 0:
        return None, {
            "row": row,
            "reason": "A darabszám nulla vagy negatív"
        }
    
    total_price = product_amount * product_price

    return {
        "product_name": product_name,
        "product_amount": product_amount,
        "product_price": product_price,
        "total": total_price
    }, None


def service():
    
    raw_products = [
    "apple; 12 ; 350",
    "banana; 5 ; 420",
    "milk; 2 ; 690",
    "bread; 0 ; 850",
    "cheese; 3 ; 1490",
    "invalid row",
    "orange; 8 ; 390"
    ]

    valid_products = []
    invalid_products = []

    for row in raw_products:
        product, error = parse_product(row)
        
        if error is not None:
            invalid_products.append(error)
        else:
            valid_products.append(product)
    
    return valid_products, invalid_products
        

if __name__ == "__main__":

    valid_products, invalid_products = service()

    teljes_keszletertek = 0

    print("===== Leltár =====")
    print("Hiba nélkül nyilvántartásban levő termékek:")
    for product in valid_products:
        termek_osszesitett_ertek = product['product_amount'] * product['product_price']
        print(f"{product['product_name']} - {product['product_amount']} db - {product['product_price']} Ft/db - összesen: {termek_osszesitett_ertek} Ft")
        teljes_keszletertek = teljes_keszletertek + termek_osszesitett_ertek

    print("Hibásan szereplő termékek:")
    for invalid_product in invalid_products:
        print(f"{invalid_product['row']} -> {invalid_product['reason']}")

    
    print(f"Teljes készletérték: {teljes_keszletertek}")