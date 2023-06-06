import pandas as pd

# CSV fájl beolvasása
data = pd.read_csv('adatok.csv')

# Hiányzó értékek kezelése
data = data.fillna(0)  # Hiányzó értékek feltöltése nullával

# Oszlopok átnevezése
data = data.rename(columns={'regi_oszlop_nev': 'uj_oszlop_nev'})

# Oszlopok átrendezése
data = data[['oszlop1', 'oszlop2', 'oszlop3']]

# Outlier-ek kezelése
def outlier_kezeles(sor):
    if sor['oszlop3'] > 1000:
        return 1000
    else:
        return sor['oszlop3']

data['oszlop3'] = data.apply(outlier_kezeles, axis=1)

# Tisztított adatkészlet kiíratása
print(data.head())