##  Import packages
import csv
import pandas as pd
import pickle
from dask import delayed, compute

from functions import similar, lists_combinations


## eu_title
df_eu = pd.read_csv('../trial_title/eu_title.csv', sep='|')
##TEST
#df_eu = df_eu[0:100]

# Add an indicator column
df_eu['trial_indicator'] = 'EU'

### ictrp_titles
df_ictrp = pd.read_csv('../trial_title/ictrp_title.csv', sep='|')
##TEST
#df_ictrp = df_ictrp[0:100]

# Add an indicator column
df_ictrp['trial_indicator'] = 'ICTRP'


### LIST EU ICTRP LONG TITLES
list_long_eu = df_eu[['trial_id','trial_indicator','long_title']].apply(tuple, axis=1).tolist()
list_long_ictrp = df_ictrp[['trial_id','trial_indicator','long_title']].apply(tuple, axis=1).tolist()

list_eu_ictrp_long = delayed(lists_combinations)(list_long_eu,list_long_ictrp)
list_eu_ictrp_long.compute()


with open('../results/Pickles/list_eu_ictrp_long_titles.pickle', 'wb') as f:
   pickle.dump(list_eu_ictrp_long, f)