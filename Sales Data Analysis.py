import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
sales_data = pd.read_csv('sales_data.csv')

# Calculate total revenue per product
sales_data['Revenue'] = sales_data['Quantity'] * sales_data['Price']
product_revenue = sales_data.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

# Identify peak sales periods
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
monthly_sales = sales_data.groupby(sales_data['Date'].dt.to_period('M'))['Revenue'].sum()

# Plotting
product_revenue.plot(kind='bar', color='green', title='Total Revenue by Product')
plt.ylabel('Revenue')
plt.show()

monthly_sales.plot(kind='line', title='Monthly Sales Trends')
plt.ylabel('Revenue')
plt.show()
