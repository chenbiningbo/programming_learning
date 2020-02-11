import pandas as pd
from pandas import Series
from pandas import DataFrame

# Write your code here
obj = Series([4, 7, -5, 3])
print(obj)

L = Series(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
print(L)


L1 = Series(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], index=[2, 3, 4, 5, 6, 7, 1])
print(L1)