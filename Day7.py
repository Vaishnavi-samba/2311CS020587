// Load and explore the data

import pandas as pd

# Load the dataset
file_path = 'sales_data.csv'  # Replace with the actual path to your file
sales_data = pd.read_csv(file_path)

# Display the first 5 rows of the dataset
print("First 5 rows of the dataset:")
print(sales_data.head())

# Print basic statistics of numerical columns
print("\nBasic statistics of numerical columns:")
print(sales_data.describe())




// Data Analysis

# Calculate the total sales for each region
total_sales_by_region = sales_data.groupby('Region')['Sales'].sum()
print("Total sales for each region:")
print(total_sales_by_region)

# Find the most sold product (based on quantity)
most_sold_product = sales_data.groupby('Product')['Quantity'].sum().idxmax()
most_sold_quantity = sales_data.groupby('Product')['Quantity'].sum().max()
print("\nMost sold product:")
print(f"Product: {most_sold_product}, Quantity: {most_sold_quantity}")

# Compute the average profit margin for each product
sales_data['Profit Margin (%)'] = (sales_data['Profit'] / sales_data['Sales']) * 100
average_profit_margin_by_product = sales_data.groupby('Product')['Profit Margin (%)'].mean()
print("\nAverage profit margin for each product:")
print(average_profit_margin_by_product)
