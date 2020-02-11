import pandas as pd

df = pd.read_csv('csv/399300.csv', encoding='gbk')[['date', 'close', 'change']]
print(df)