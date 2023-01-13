import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

path = 'winemag-data-130k-v2.csv'
df = pd.read_csv(path,index_col=0)
print(df)
# print(df.description)
print(df.iloc[[3,10],1:3])
print(df.loc[1:8,'country':'province'])
