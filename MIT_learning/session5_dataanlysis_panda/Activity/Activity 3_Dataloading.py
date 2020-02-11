import pandas as pd
from pandas import Series
from pandas import DataFrame

# Read the data from the Excel file: sales.xlsx
# FIX_ME
data2 = pd.read_excel("../sales_data.xlsx")


# Display the first 10 rows
print(data2.head(10))


# Display the last 10 rows
print(data2.tail(10))


# Return a tuple with the number of rows and columns
print(data2.shape)


# Return the column data types
print(data2.info())

# Save the DataFrame as a CSV file.
data2.to_csv("../sales_data.csv")