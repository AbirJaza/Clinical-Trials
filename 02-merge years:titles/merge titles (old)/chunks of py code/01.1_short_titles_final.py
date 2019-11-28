##  Import packages
import csv
import pandas as pd
import pickle
from dask import delayed, compute

from functions import similar, lists_combinations


## us_titles
#df_us = pd.read_csv("../trial_title/us_title.csv", sep='|')
df_us = pd.read_csv("../trial_title/chunks/US/0001.csv", sep='|')
##TEST
#df_us = df_us[0:100]  

# Add an indicator column
df_us['trial_indicator'] = 'US'

### ictrp_titles
#df_ictrp = pd.read_csv('../trial_title/ictrp_title.csv', sep='|')
df_ictrp = pd.read_csv('../trial_title/chunks/ICTRP/0001.csv', sep='|')
##TEST
#df_ictrp = df_ictrp[0:100]

# Add an indicator column
df_ictrp['trial_indicator'] = 'ICTRP'


### LIST SHORT TITLES
list_short_us = df_us[['trial_id','trial_indicator','short_title']].apply(tuple, axis=1).tolist()
list_short_ictrp = df_ictrp[['trial_id','trial_indicator','short_title']].apply(tuple, axis=1).tolist()

list_short_title = delayed(lists_combinations)(list_short_us,list_short_ictrp)
list_short_title.compute()


# Final short tilte table
df_all_short_titles = pd.DataFrame(list_short_title.compute(), columns=['id1_id2', 'indicator1_indicator2', 'shorttitle1_shorttitle2', 'similarity'])

df_all_short_titles.to_csv('../results/short_titles.csv', sep='|')

with open('../results/Pickles/df_all_short_titles.pickle', 'wb') as f:
   pickle.dump(df_all_short_titles, f)