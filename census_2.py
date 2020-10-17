import numpy as np
import pandas as pd
import pandasql as ps
import glob

# Question 4: find the changes between 2011 and 2016
# load the combined csv into a DataFrame
df = pd.read_csv("combined_csv.csv", index_col=0)

# % of change

# 1: drop column that has the "total" because those are subtotal
# source: https://stackoverflow.com/questions/38383886/drop-column-based-on-a-string-condition 
df_drop = df.drop([col for col in df.columns if 'Tot_Resp' in col],axis=1,inplace=True)

# 2: find the % change for each ancestry nationalities
res = df.pct_change().mul(100).round(3)  # result is in %

# 3: replace inf or -inf value with NaN
df_res_nan = res.replace([np.inf, -np.inf], np.nan)

# find the ancestry that have the biggest change between 2011 and 2016
df_res_nan['Max'] = df_res_nan.idxmax(axis=1)
print(df_res_nan)

# 4: Get the % of the result
maxValuesObj = df_res_nan.max(axis=1)
print('Maximum value: ')
print(maxValuesObj)