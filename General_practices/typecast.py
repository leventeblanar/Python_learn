#  typecast: az egyik leggyakoribb hibaforrás
#  adott adatok adott típusra való formázása az egyeztetések végett

#  alap python typecastolás:
int("42")       # 42
float("3.14")   # 3.14
str(100)        # "100"
list("abc")     # ['a', 'b', 'c']
tuple([1, 2])   # (1, 2)
set([1, 2, 2])  # {1, 2}


"""
Python type conversion
- Python esetén két typeconv létezik:
    - implicit (automatikus)
        Ebben az esetben az a type győz amelyik magasabb rendű. Pl int + float esetén float, hogy elkerüljük az adatvesztést
    - explicit (manuális)
        Manuális konverzió esetén szokás ezt typecast-nek hívni
        num_int = int(num_string)
"""


#  pandas specifikus typecast

import pandas as pd
import re

def pandas_cast_1():
    df = pd.DataFrame({"szamok": ["1", "2", "3"]})
    df["szamok"] = df["szamok"].astype(int)
    print(df.dtypes)


def pandas_cast_2():
    df = pd.DataFrame({"adat": ["10", "20", "alma"]})
    df['adat_szam'] = pd.to_numeric(df["adat"], errors="coerce")
    print(df)


#  ----- GYAKORLÓS -----

def safe_float(x):

    try:
        return float(x)
    except (ValueError, TypeError):
        return None

# print(safe_float("3.14"))
# print(safe_float("alma"))
# print(safe_float(42))

def typecast_list():

    adatok = ["3.14", "42", "x", None, "100.5"]
    new_adatok = []

    for adat in adatok:
        new_adat = safe_float(adat)
        new_adatok.append(new_adat)

    print(new_adatok)


def typecast_list2():

    adatok = ["3.14", "42", "x", None, "100.5"]
    new_adatok = [safe_float(adat) for adat in adatok]
    print(new_adatok)


def typecast_list3():

    adatok = ["100", " 200 Ft", "", "x", "300,5", None]
    tisztitott = []

    for adat in adatok:
        if adat is None:
            tisztitott.append(None)
            continue

        clean_str = re.sub(r"[^\d\.\-]", "", str(adat)).replace(",", ".")
        if clean_str == "":
            tisztitott.append(None)
        else:
            tisztitott.append(safe_float(clean_str))

    print(tisztitott)


def typecast_pandas_1():

    df = pd.DataFrame({
        "ar": ["100 Ft", "200,50", "300.00", "x", "", None, "-150 Ft"]
    })

    s = df['ar'].astype('string')
    s = s.str.replace(",", ".", regex=False)
    s = s.str.replace(r"[^\d\.\-]", "", regex=True)
    s = s.replace("", pd.NA)
    num = pd.to_numeric(s, errors='coerce')
    df['ar_tiszta'] = num.astype("Int64")

    hibas_maszk = df['ar_tiszta'].isna()
    if hibas_maszk.any():
        print("Hibás/konvertálhatatlan értékek:")
        print(df.loc[hibas_maszk, "ar"].to_list())
    
    print(df)
    return df

def typecast_pandas_2():

    df = pd.DataFrame({"ar": ["100 Ft", "200,50", "300.00", "x", "", None, "-150 Ft"]})
    df['ar_tiszta'] = (pd.to_numeric(
        df['ar'].astype("string")
                .str.replace(",", ".", regex=False)
                .str.replace(r"[^\d\.\-]", "", regex=True)
                .replace("", pd.NA),
        errors='coerce')
        .astype("Int64")
    )
    print(df)


def typecast_pandas_3():

    df = pd.DataFrame({
    "datum": [
        "2021-01-01",
        "2021/02/15",
        "15-03-2021",
        "rossz_datum",
        "",
        None,
        "2021.04.01"
    ]
    })

    df['datum_tiszta'] = (pd.to_datetime(df['datum'], errors='coerce', dayfirst=True))
    mask_feb_2021 = (df['datum_tiszta'].dt.year == 2021) & (df["datum_tiszta"].dt.month == 2)
    feb = df.loc[mask_feb_2021]

    print(df)
    print("\n2021 február:")
    print(feb)
    return df, feb


def typecast_pandas_4():

    df = pd.DataFrame({
        "ido": [
            "2:30:00",
            "90m",
            "01:15",
            "rossz_ido",
            "",
            None,
            "0:45:00"
        ]
    })

    df['ido_td'] = (pd.to_timedelta(df['ido'], errors='coerce'))
    mask = df["ido_td"] > pd.Timedelta(hours=1)
    more_than_1 = df.loc[mask]

    print(more_than_1)
    return df, more_than_1


def typecast_pandas_5():

    df = pd.DataFrame({
        "ido": [
            "2021-01-01 12:30:00",
            "2021/02/15 08:00",
            "15-03-2021 14:45",
            "rossz_ido",
            "",
            None,
            "2021.04.01 23:59"
        ]
    })

    df['ido_td'] = pd.to_datetime(df['ido'], errors='coerce', dayfirst=True)

    mask = (df["ido_td"].dt.year == 2021) & (df['ido_td'].dt.month == 3)
    march_2021 = df.loc[mask]

    print(march_2021)
    return df, march_2021


#  ----- REVIEW -----

def safe_float(data):
    try:
        return float(data)
    except (ValueError, TypeError):
        return None
    

def direct_typeconv():
    df = {"ar": 10.00}

    df["ar"] = df["ar"].astype(int)

def to_numeric():
    df = pd.DataFrame({
        "ar": ["100", "200", "x", "", None, "300.5"]
    })

    df["ar_szam"] = pd.to_numeric(df["ar"], errors="coerce")

    print(df)
    print(df.dtypes)


def to_datetime():
    df = pd.DataFrame({
        "datum": [
            "2021-01-01",
            "2021/02/15",
            "15-03-2021",
            "rossz",
            "",
            None
        ]
    })

    df["datum_dt"] = pd.to_datetime(df["datum"], errors="coerce", dayfirst=True)

    print(df)
    print(df.dtypes)


def to_timedelta():

    df = pd.DataFrame({
    "ido": ["2:30:00", "90m", "01:15", "rossz", "", None]
    })

    df["ido_td"] = pd.to_timedelta(df["ido"], errors="coerce")

    print(df)
    print(df.dtypes)


