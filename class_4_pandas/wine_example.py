import pandas as pd

path = 'winemag-data-130k-v2.csv'
df = pd.read_csv(path)
print(df.head(3))
print(df.shape)
