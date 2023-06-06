import pandas as pd
from sklearn.linear_model import LinearRegression

# Adatok betöltése
data = pd.read_csv('adatok.csv')

# Független változók és célváltozó kiválasztása
X = data[['fuggetlen_valtozo1', 'fuggetlen_valtozo2']]
y = data['celvaltozo']

# Modell illesztése
model = LinearRegression()
model.fit(X, y)

# Predikció
pred = model.predict(X)

# Predikciók kiíratása
print(pred)