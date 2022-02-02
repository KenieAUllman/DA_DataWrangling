import numpy as np
import pandas as pd
import matplotlib.pylab as plt


df = pd.read_csv('Schools.csv')
#assigns the csv file to a dataframe

df.shape 
#returns a tuple representing dimenionality of the dataframe

df.info()
# returns the information on my dataframe

df.describe 
# generates some general descriptie statistics 

df.head(n=5)
# returns the first 5 rows

dft = df.T
# assigns 'transpose' to another variable to use later

dft.columns
# transposes by columns

df[["Campus Name", "Zip Codes", "Supervisor Districts"]]
# two square brackets allows me to pass a list to the index

df.iloc[[4,2]]
# integer based indexing and will return rows 4 and 2

df["Supervisor Districts"] > 3 
# will filter my information, making it return all 
# rows that have a 'Supervisor District' above 3

df.sort_index(axis=1)
#sorts objects by labels along an axis 

df.sort_values(by="Zip Codes")
# sort my index by the rows of zip codes 

df.sort_values(by="Supervisor Districts")
# sort my index by Supervisor districts in lowest integer to largest

#df.isnull().any()
# checks if any of my columns contain missing information
# my data is missing infomation in the CDS code, fire prevention districts, 
# and police districts

#df.insnull().all(axis=1).any()
#isnull checks that my DataFrame is true for every null value, then we check 
# every row to see if it is all true with axis=1. Lastly we call any on those 
# series of true and false values to see if it contains any true values
# so I know I don't have any rows that are completely empty; I could also use
# notnull which does the opposite of isnull

#df.loc[df.isnull().any(axis=1), 'Fire Prevention Districts'].value_counts()
# this searches the column I listed for any null values and provides their count

rows_to_fill = df.isnull().any(axis=1)

print()