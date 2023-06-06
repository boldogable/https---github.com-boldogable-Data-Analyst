import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
# Read CSV file
data = pd.read_csv(file_path)
return data

def display_overview(data):
# Overview of the data
print(data.head())

def extract_summary(data):
# Extract statistical information
summary = data.describe()
return summary

def extract_column(data, column_name):
# Extract a specific column
column = data[column_name]
return column

def visualize_data(data, column_name):
# Data visualization
data[column_name].plot(kind='hist')
plt.show()

def main():

# Load the data
file_path = 'data.csv'
data = load_data(file_path)
# Display overview
display_overview(data)

# Extract summary
summary = extract_summary(data)
print(summary)

# Extract a specific column
column_name = 'column_name'
column = extract_column(data, column_name)
print(column)

# Visualize data
visualize_data(data, column_name)
if name == 'main':
main()
