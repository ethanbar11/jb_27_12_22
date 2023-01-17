import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

path = 'winemag-data-130k-v2.csv'
df = pd.read_csv(path, index_col=0)

mask = (df.country == 'Israel')
print(df[mask])
# mask = df.country.isin(['Israel','Italy'])
# mask = ~(df.price.notnull())
# df.taster_name = 'Bla Bla'
# print(df)
# print(mask)
# df[mask] = 100
# print(df[mask])
