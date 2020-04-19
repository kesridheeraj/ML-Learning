import pandas
from sklearn import datasets
# var = datasets.load_boston()
datafile = 'Data/forestfires.csv'
names = ['X', 'Y', 'Month', 'Day', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N8', 'N9']
df = pandas.read_csv(datafile, names = names)
#print(pandas.isnull(df))
# print(df.head(15))
df.Day.replace(('mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'), (1, 2, 3, 4, 5, 6, 7), inplace=True)
df.Month.replace(('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), inplace=True)
print('******************')
# print(df.head(15))
print(df.dtypes)
print(df.describe())