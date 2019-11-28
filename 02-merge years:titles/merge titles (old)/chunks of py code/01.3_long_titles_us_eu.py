##  Import packages
import csv
import pandas as pd
import pickle
from dask import delayed, compute

from functions import similar, lists_combinations


## us_titles
df_us = pd.read_csv('../trial_title/us_title.csv', sep='|')
##TEST
#df_us = df_us[0:100]

# Add an indicator column
df_us['trial_indicator'] = 'US'

## eu_title
df_eu = pd.read_csv('../trial_title/eu_title.csv', sep='|')
##TEST
#df_eu = df_eu[0:100]

# Add an indicator column
df_eu['trial_indicator'] = 'EU'


### LIST US EU LONG TITLES
list_long_us = df_us[['trial_id','trial_indicator','long_title']].apply(tuple, axis=1).tolist()
list_long_eu = df_eu[['trial_id','trial_indicator','long_title']].apply(tuple, axis=1).tolist()

list_us_eu_long = delayed(lists_combinations)(list_long_us,list_long_eu)
list_us_eu_long.compute()


with open('../results/Pickles/list_us_eu_long_titles.pickle', 'wb') as f:
   pickle.dump(list_us_eu_long, f)