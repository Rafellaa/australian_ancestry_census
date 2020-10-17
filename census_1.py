import numpy as np
import pandas as pd
import pandasql as ps
import glob

# # Question 3

# funtion 1
def clean_data(filename):

    # Step 1: load the data
    df_initial = pd.read_csv(filename)

    # if statement for step 2 and 3
    if filename == "2016Census_G08_NSW_POA.csv":

        # Step 2: Drop the column that does not a match in both files
        df_drop = df_initial.drop([col for col in df_initial.columns if 'Sri_Lankan' in col],axis=1)
        df_clean = df_drop[df_drop.columns[:-6]]

        # Step 3: rename the column so that both files have the same naming conventions
        df_clean.rename(columns={"POA_CODE_2016": "region_id"}, inplace=True)

        # Step 4: find data with postcode of 2577 and put it to a CSV file so we can convert it to DataFrame for later uses
        sql_2577 = ps.sqldf("SELECT * FROM df_clean WHERE region_id = 'POA2577'")

        # Step 5: save the file
        sql_2577.to_csv(csv_filename_2016)
        df_2577 = pd.read_csv(csv_filename_2016)

        print('File is 2016')

    else:

        # merge file A and B to one
        df1 = pd.read_csv('2011Census_B08A_NSW_POA_short.csv')
        df2 = pd.read_csv('2011Census_B08B_NSW_POA_short.csv')

        df_merged = df1.merge(df2, on='region_id')

        df_drop = df_merged.drop([col for col in df_merged.columns if 'Sinhalese' in col],axis=1)
        df_clean = df_drop[df_drop.columns[:-12]]

        sql_2577 = ps.sqldf("SELECT * FROM df_clean WHERE region_id = 'POA2577'")
        sql_2577.to_csv(csv_filename_2011)
        df_2577 = pd.read_csv(csv_filename_2011)

        print('File is 2011')

# set up all the variables needed
filenames = sorted(glob.glob('*Census*.csv'))

csv_filename_2011 = "KV_2011.csv"
csv_filename_2016 = "KV_2016.csv"

# using the functions
for filename in filenames[:]:
    print(filename)
    clean_data(filename)









# function 2
def rename(filename):
    # Step 1: load the data
    df_initial = pd.read_csv(filename)

    # Steo 2: add column called year and put the year there
    df_initial.rename( columns={'Unnamed: 0':'year'}, inplace=True )

    if filename == "KV_2016.csv":
        df_initial.year = '2016'
        df_initial.to_csv("2016_clean.csv")

        print("2016 is cleaned")
    else:
        df_initial.year = '2011'
        df_initial.to_csv("2011_clean.csv")

        print("2011 is cleaned")

filenames_clean = sorted(glob.glob('KV*.csv'))

# using the functions
for filename in filenames_clean[:]:
    print(filename)
    rename(filename)





# combine both 2011 and 2016 clean data using UNION sql 
df_KV2011 = pd.read_csv('2011_clean.csv')
df_KV2016 = pd.read_csv('2016_clean.csv')
combined_csv = ps.sqldf("SELECT * FROM df_KV2011 UNION SELECT * FROM df_KV2016")
combined_csv.drop(['Unnamed: 0', 'region_id'], axis=1, inplace = True)

#export to csv
combined_csv.to_csv( "combined_csv.csv")




    

