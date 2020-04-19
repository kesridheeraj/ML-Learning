import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
auto_data = pd.read_csv('Data/02/demos/data/imports-85.data', sep=',', engine='python')
#print(auto_data)
auto_data = auto_data.replace('?', np.nan)
print(auto_data)
print(auto_data.describe())
print(auto_data.dtypes)