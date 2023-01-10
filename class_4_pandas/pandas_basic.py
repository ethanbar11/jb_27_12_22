import pandas as pd

data = {'Ethan Grades': [100, 100, 100], 'Omry Grades': [50, 60, 90], 'Bla Grades': [40, 30, 100]}
print(pd.DataFrame(data, index=['Math', 'English', 'Science']))
