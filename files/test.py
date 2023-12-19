# import pandas as pd
# 
# data = pd.Series([1, 2, 3])
# print(data)


import pandas as pd

import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())