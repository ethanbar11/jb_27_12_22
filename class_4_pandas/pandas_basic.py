import pandas as pd

data = {'Ethan Grades': [100, 100, 100], 'Omry Grades': [50, 60, 90], 'Bla Grades': [40, 30, 100]}
df = pd.DataFrame(data, index=['Math', 'English', 'Science'])
df.to_csv('my_grades.csv')
# print(df)
print(df['Omry Grades'])
s = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
print(s)