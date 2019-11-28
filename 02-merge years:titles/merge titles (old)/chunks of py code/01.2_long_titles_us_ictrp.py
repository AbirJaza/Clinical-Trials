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

### ictrp_titles
df_ictrp = pd.read_csv('../trial_title/ictrp_title.csv', sep='|')
##TEST
#df_ictrp = df_ictrp[0:100]

# Add an indicator column
df_ictrp['trial_indicator'] = 'ICTRP'


### LIST US ICTRP LONG TITLES
list_long_us = df_us[['trial_id','trial_indicator','long_title']].apply(tuple, axis=1).tolist()
list_long_ictrp = df_ictrp[['trial_id','trial_indicator','long_title']].apply(tuple, axis=1).tolist()

list_us_ictrp_long = delayed(lists_combinations)(list_long_us,list_long_ictrp)
list_us_ictrp_long.compute()


with open('../results/Pickles/list_us_ictrp_long_titles.pickle', 'wb') as f:
   pickle.dump(list_us_ictrp_long, f)