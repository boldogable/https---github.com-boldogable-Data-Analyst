import pandas as pd

def load_data(file_path):
# Read CSV file
data = pd.read_csv(file_path)
return data

def handle_missing_values(data):
# Fill missing values with zero
data = data.fillna(0)
return data

def rename_columns(data, column_mapping):
# Rename columns based on the provided mapping
data = data.rename(columns=column_mapping)
return data

def reorder_columns(data, column_order):
# Reorder columns based on the provided order
data = data[column_order]
return data

def handle_outliers(data, column_name, threshold):
# Handle outliers in the specified column
data.loc[data[column_name] > threshold, column_name] = threshold
return data

def main():
# Load the data
file_path = 'data.csv'
data = load_data(file_path)

# Handle missing values
data = handle_missing_values(data)

# Rename columns
column_mapping = {'old_column_name': 'new_column_name'}
data = rename_columns(data, column_mapping)

# Reorder columns
column_order = ['column1', 'column2', 'column3']
data = reorder_columns(data, column_order)

# Handle outliers
column_name = 'column3'
threshold = 1000
data = handle_outliers(data, column_name, threshold)

# Print the cleaned dataset
print(data.head())
if name == 'main':
main()
