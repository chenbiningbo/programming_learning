
import pandas as pd
from pandas import Series
from pandas import DataFrame

# Create a dictionary of the time series (the keys are "month" and "demand")
Time_Series = {"Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"], "Demand": [50, 70, 65, 45, 60, 75]}
data = DataFrame(Time_Series)
print(data)


# Add a column to the DataFrame corresponding to the year
data['year'] = 2018

print(data)


data1 = data[["year", "Month", "Demand"]].copy()
print(data1)


# Convert demand values to a list
print(data["Demand"].tolist())