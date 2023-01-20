import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

path = 'winemag-data-130k-v2.csv'
df = pd.read_csv(path, index_col=0)
print(df)
df = df.set_index('title')
print(df.title.loc['Quinta dos Avidagos 2011 Avidagos Red (Douro)'])
# print(df.loc['Quinta dos Avidagos 2011 Avidagos Red (Douro)'])