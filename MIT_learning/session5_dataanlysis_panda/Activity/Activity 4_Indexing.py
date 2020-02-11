import pandas as pd
from pandas import Series
from pandas import DataFrame

# Read the data from the Excel file: sales.xlsx
data2 = pd.read_excel("../sales_data.xlsx")


# Create a new column that contains the profit per SKU unit (price minus cost).
data2['profit_per_SKU'] = data2['Price']-data2['Cost']
# print(data2.head(3))

# Return the data of the first row using iloc()
# print(data2.iloc[0, :])


# Return the data of the first row using head()
# print(data2.head(0))


# Return data of just the 'Sales' and 'Dev' columns as a DataFrame
# print(data2[['Sales', 'Dev']])


# Return SKUs (rows) for which sales are greater than 50
data3 = data2[data2['Sales']>50]
print(data3['SKU'])


# Return SKUs (rows) for which sales are greater than 50 AND standard deviation (Dev) is smaller than 20.
data4=data2[(data2['Sales']>50)&(data2['Dev']<20)]
print(data4)

# In one line of code, create a new DataFrame of the SKUs (rows) for sales are greater than 50 AND
# standard deviation (Dev) is smaller than 20, outputting only the "cost" and "price" columns.
print(data4[['Cost','Price']])