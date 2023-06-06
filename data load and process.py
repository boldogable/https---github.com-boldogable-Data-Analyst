import pandas as pd

# CSV fájl beolvasása
data = pd.read_csv('adatok.csv')

# Adatok áttekintése
print(data.head())

# Statisztikai információk kinyerése
summary = data.describe()
print(summary)

# Adott oszlop kiemelése
column = data['oszlop_neve']
print(column)

# Adatok vizualizációja
data['oszlop_neve'].plot(kind='hist')