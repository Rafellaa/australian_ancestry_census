import numpy as np
import pandas as pd
import pandasql as ps
import glob

# proportional value for each category to know how many % of people are this type of ancestry on 2011 and 2016

df = pd.read_csv("combined_csv.csv")

# 1: drop column that has the "total" because those are subtotal
# source: https://stackoverflow.com/questions/38383886/drop-column-based-on-a-string-condition 
df.drop([col for col in df.columns if 'Tot_Resp' in col],axis=1,inplace=True)

# 2: find the percentage of each ancestry's response each row
# source: https://stackoverflow.com/questions/50820659/compute-row-percentages-in-pandas-dataframe 
df = df.set_index('year')
res = df.div(df.sum(axis=1), axis=0).mul(100).round(3) 

# find the ancestry that have the most people in Kangaroo Valley
res['Max'] = res.idxmax(axis=1)
print(res)

# Get the % of the result
maxValuesObj = res.max(axis=1)
print('Maximum value: ')
print(maxValuesObj)