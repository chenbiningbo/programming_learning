import pandas as pd
from pandas import Series
from pandas import DataFrame

# Read the data from the Excel file: sales.xlsx
data2 = pd.read_excel("../sales_data.xlsx")

# Create a new column that contains the profit per SKU unit (price minus cost).
data2['profit_per_SKU'] = data2['Price'] - data2['Cost']
# print(data2.head(3))

# Sort the SKUs (rows) by sales in descending order
data2 = data2.sort_values(ascending=False, by='Sales')

# Delete the column 'profit' in one line of code
data2 = data2.drop(columns=['profit_per_SKU'])

# Display the first ten rows of the data set
print(data2.head(10))
