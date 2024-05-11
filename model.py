import pandas as pd

# Create a simple dataframe
data = {
    'Material': ['Material1', 'Material2', 'Material3', 'Material4', 'Material5'],
    'Density': [2.7, 7.9, 1.5, 8.9, 2.3],
    'Hardness': [3.0, 8.0, 2.5, 9.0, 3.5],
    'Melting_Point': [660, 1510, 170, 960, 650]
}

df = pd.DataFrame(data)

# Save the dataframe to a CSV file
df.to_csv('materials_data.csv', index=False)

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('materials_data.csv')

# Display the first 5 rows of the dataframe
print(df.head())

# Basic statistics of the dataframe
print(df.describe())

# Density vs Hardness
density_vs_hardness = df[['Density', 'Hardness']]
print(density_vs_hardness)
