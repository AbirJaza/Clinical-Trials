##  Import packages

import csv
import pandas as pd
from difflib import SequenceMatcher
import itertools
from fuzzywuzzy import fuzz, process
import pickle

### calculate simularity
def similar(a, b):
    return SequenceMatcher(lambda x: x == " ", a, b).ratio()

def lists_combinations(list1,list2):
    combination_list = []
    for i in list1:
        for j in list2: 
            similarity = similar(str(i[2]),str(j[2]))
            if (similarity > 0.85) :
                trial_id = str(i[0])+' _ '+str(j[0])
                trial_indicatror = str(i[1])+' _ '+str(j[1])
                title = str(i[2])+' _ '+str(j[2])

                new_tuple = (trial_id,trial_indicatror, title, similarity)
                combination_list.append(new_tuple)
    return(combination_list)

## us_title
df_us = pd.read_csv('us_title.csv', sep='|')
# Add an indicator column
df_us['trial_indicator'] = 'US'

## eu_title
df_eu = pd.read_csv('eu_title.csv', sep='|')
# Add an indicator column
df_eu['trial_indicator'] = 'EU'

### ictrp_title
df_ictrp = pd.read_csv('ictrp_title.csv', sep='|')
# Add an indicator column
df_ictrp['trial_indicator'] = 'ICTRP'

### LIST SHORT TITLES
list_short_us = df_us[['trial_id','trial_indicator','short_title']].apply(tuple, axis=1).tolist()

list_short_ictrp = df_ictrp[['trial_id','trial_indicator','short_title']].apply(tuple, axis=1).tolist()

list_short_title = lists_combinations(list_short_us,list_short_ictrp)

# Final short tilte table
df_all_short_titles = pd.DataFrame(list_short_title, columns=['id1_id2', 'indicator1_indicator2', 'shorttitle1_shorttitle2', 'similarity'])


with open('df_all_short_titles.pickle', 'wb') as f:
   pickle.dump(df_all_short_titles, f)


### LIST LONG TITLES
list_long_us = df_us[['trial_id','trial_indicator','long_title']].apply(tuple, axis=1).tolist()

list_long_ictrp = df_ictrp[['trial_id','trial_indicator','long_title']].apply(tuple, axis=1).tolist()

list_long_eu = df_eu[['trial_id','trial_indicator','long_title']].apply(tuple, axis=1).tolist()

list_long_us_ictrp = lists_combinations(list_long_us,list_long_ictrp)

list_long_us_eu = lists_combinations(list_long_us,list_long_eu)

list_long_ictrp_eu = lists_combinations(list_long_ictrp,list_long_eu)

list_long_title = list_long_us_ictrp + list_long_us_eu + list_long_ictrp_eu

## Final long tilte table
df_all_long_titles = pd.DataFrame(list_long_title, columns=['id1_id2', 'indicator1_indicator2', 'longtitle1_longtitle2', 'similarity'])


with open('df_all_long_titles.pickle', 'wb') as f:
   pickle.dump(df_all_long_titles, f)
