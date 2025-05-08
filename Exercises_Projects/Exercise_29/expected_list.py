


def check_expected():

    expected_items = ["ABC123", "DEF456", "GHI789", "JKL000"]
    actual_items = ["DEF456", "GHI789"]

    missing_items = []
    
    for item in expected_items:
        if item not in actual_items:
            print(f"Missing item: {item}")
            missing_items.append(item)

    print(len(missing_items))
    print(f"Missing items: ", missing_items)





def valid_cikkszam():

    item_list = ["ABC123", "", "X1", "123456", "GHI789", "?!?", "ZXC999"]

    valid = []
    invalid = []

    for item in item_list:
        if len(item) == 6 and item.isalnum():
            valid.append(item)
        else:
            invalid.append(item)
    
    print("Érvényes cikkszámok: ", valid)
    print("Érvénytelen cikkszámok: ", invalid)


valid_cikkszam()