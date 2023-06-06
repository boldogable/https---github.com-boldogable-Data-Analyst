import pandas as pd
import matplotlib.pyplot as plt

# Adatok betöltése
data = pd.read_csv('adatok.csv')

# Adatok vizualizációja
plt.bar(data['oszlop_nev'], data['ertek'])
plt.xlabel('Oszlop neve')
plt.ylabel('Érték')
plt.title('Adatok vizualizációja')

# Diagram megjelenítése
plt.show()