import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

path = 'winemag-data-130k-v2.csv'
df = pd.read_csv(path, index_col=0)
# print(df.iloc[df.groupby('country').points.idxmax()])
# print(df.groupby('points').price.min())
print(df.country.iloc[0])
print(df.sort_values('country', ascending=True))
