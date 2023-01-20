import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

path = 'winemag-data-130k-v2.csv'
df = pd.read_csv(path, index_col=0)


def return_value_power_by_2(x):
    return x ** 2


points_mean = df.points.mean()

print(df.price - points_mean)

# def decrease_point_mean(x):
#     return x - points_mean
#
# print(df.title.unique())

# print('The average of points is', points_mean)
# print(pd.concat((df.points, df.points.map(decrease_point_mean)), axis='columns'))
# print('The average of points after map is',df.points.map(decrease_point_mean).mean())
