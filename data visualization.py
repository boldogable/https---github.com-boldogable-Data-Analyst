import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
# Load data from CSV file
data = pd.read_csv(file_path)
return data

def visualize_data(data, column_name, value_name):
# Data visualization
plt.bar(data[column_name], data[value_name])
plt.xlabel(column_name)
plt.ylabel(value_name)
plt.title('Data Visualization')

bash
Copy code
# Show the plot
plt.show()
def main():
# Load the data
file_path = 'data.csv'
data = load_data(file_path)

kotlin
Copy code
# Visualize data
column_name = 'column_name'
value_name = 'value'
visualize_data(data, column_name, value_name)
if name == 'main':
main()
