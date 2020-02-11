import pandas as pd
from pandas import Series
from pandas import DataFrame

# Read the data from the Excel file: sales.xlsx
data2 = pd.read_excel("../sales_data.xlsx")

# Count the number of SKUs
print(data2['SKU'].count())

# Caculate total sales (sum all sales)
print(data2['Sales'].sum())

# Find the average price
print(data2['Price'].mean())

# Return the index of the row with the highest cost (in one line of code)
print(data2['Cost'].idxmax())

# Return the index of the row with the lowest cost (in one line of code)
print(data2['Cost'].idxmin())

# Return the SKU with the lowest price (in one line of code)
data2.iloc[data2['Price'].idxmin()]
