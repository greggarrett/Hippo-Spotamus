import pandas as pd
import numpy as nm
mydf = pd.read_csv('data.csv')
mydf.columns = mydf.columns.map(lambda capital: capital.capitalize())
print(mydf)

