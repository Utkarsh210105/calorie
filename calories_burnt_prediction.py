import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'calories_burnt_data.csv'  # Adjust this path if necessary
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()

# Drop unnamed columns
data = data.loc[:, ~data.columns.str.contains('^Unnamed')]

# Check the data structure
print("\nDataset Head:")
print(data.head())
print(data.info())

# Check for missing values
print("\nMissing Values in Each Column:")
print(data.isnull().sum())

# Drop rows with any missing values
data.dropna(inplace=True)

# Ensure correct data types
data['Calories Burnt'] = pd.to_numeric(data['Calories Burnt'], errors='coerce')
data['Duration'] = pd.to_numeric(data['Duration'], errors='coerce')

# Box Plot for Calories Burnt
plt.figure(figsize=(8, 6))
sns.boxplot(data=data, y='Calories Burnt')
plt.title("Box Plot of Calories Burnt")
plt.show()

# Histogram of Calories Burnt
plt.figure(figsize=(8, 6))
data['Calories Burnt'].hist(bins=20, color='skyblue')
plt.title("Histogram of Calories Burnt")
plt.xlabel("Calories Burnt")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot for Duration vs Calories Burnt
plt.figure(figsize=(8, 6))
plt.scatter(data['Duration'], data['Calories Burnt'], color='green')
plt.title("Duration vs Calories Burnt")
plt.xlabel("Duration (minutes)")
plt.ylabel("Calories Burnt")
plt.show()
