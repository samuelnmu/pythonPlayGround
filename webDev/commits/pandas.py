import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('data.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Display basic information about the dataset
print("\nBasic information about the dataset:")
print(df.info())

# Display summary statistics of the dataset
print("\nSummary statistics of the dataset:")
print(df.describe())

# Check for missing values
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Data visualization: Plotting the distribution of a specific column (e.g., 'column_name')
plt.figure(figsize=(10, 6))
df['column_name'].hist()
plt.title('Distribution of column_name')
plt.xlabel('column_name')
plt.ylabel('Frequency')
plt.show()

# Example of groupby and aggregation
print("\nGroup by a specific column and calculate mean of another column:")
grouped_data = df.groupby('group_column')['value_column'].mean()
print(grouped_data)

# Example of filtering data
print("\nFiltering the dataset for specific condition:")
filtered_data = df[df['value_column'] > threshold_value]
print(filtered_data)

# Example of creating a new column
print("\nCreating a new column based on existing columns:")
df['new_column'] = df['existing_column1'] + df['existing_column2']
print(df.head())

# Save the modified dataset to a new CSV file
df.to_csv('modified_data.csv', index=False)

print("Analysis complete, and modified dataset saved as 'modified_data.csv'.")