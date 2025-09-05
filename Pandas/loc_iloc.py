#  loc: oszlopnev alapján elérni valamit df.loc[0, "nev"]
#  iloc: sorszám/index alapján elérni valamit df.iloc[0, 0]


import pandas as pd

pelda_df = pd.DataFrame({
    "nev": ["Alex", "Bianka", "Charlie"],
    "kor": [25, 19, 32]
})


def pelda_loc():

    print(pelda_df.loc[0, "nev"] )  # sor index=0, oszlop neve="nev" → "Alex"
    print(pelda_df.loc[2, "kor"])   # sor index=2, oszlop neve="kor" → 32


def pelda_iloc():

    print(pelda_df.iloc[0, 0])   # 0. sor, 0. oszlop → "Alex"
    print(pelda_df.iloc[0, 1])   # 2. sor, 1. oszlop → 32

def pelda_3():

    print(pelda_df["nev"].iloc[0])



#  ----- GYAKORLÓS -----


df = pd.DataFrame({
    "nev": ["Alex", "Bianka", "Charlie", "Diana", "Eric", "Fiona"],
    "kor": [25, 19, 32, 28, 41, 35],
    "varos": ["Budapest", "Szeged", "Debrecen", "Pécs", "Győr", "Miskolc"],
    "fizetes": [300000, 250000, 450000, 220000, 500000, 380000]
})


def feladatok_1():

    print(df.iloc[0, 0]) # első sor (0. index) - első oszlop nev
    print(df.loc[3, "nev"])
    print(df.loc[[0, 1, 3]]) # osszes oszlop, több sor
    print(df.loc[:,['nev', 'fizetes']]) # több oszlop, összes sor
    print(df.iloc[-1]) # utolsó sor
    print(df.loc[df['fizetes'] > 350000]) # select kondíció alapján


def feladatok_2():

    print(df.iloc[[1, 2]])
    maszk = (df['fizetes']>350000) & (df['kor']<35)
    print(df.loc[maszk, ['nev','fizetes']])
    print(df.loc[[1, 3 ,5], 'nev'])
    print(df.iloc[0:3, 1:3])
    print(df.iloc[df['fizetes'].idxmax()])

feladatok_2()