import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset from the CSV file
df = pd.read_csv('sales_data.csv')

# Display the first few rows of the dataset
print(df.head())

# Data Cleaning
df.dropna(inplace=True)  # Remove missing values (not necessary here since there are no NaNs)

# Convert date column to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Extract year and month for analysis
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# Sales Trend Analysis
monthly_sales = df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()

# Visualization of Monthly Sales Trend
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', hue='Year', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title='Year')
plt.show()

# Top Selling Products
top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10).reset_index()

# Visualization of Top Products
plt.figure(figsize=(10, 5))
sns.barplot(data=top_products, x='Sales', y='Product Name', palette='viridis')
plt.title('Top 10 Selling Products')
plt.xlabel('Sales')
plt.ylabel('Product Name')
plt.show()