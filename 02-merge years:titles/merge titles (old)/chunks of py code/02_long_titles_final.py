##  Import packages
import csv
import pandas as pd
import pickle
from dask import delayed, compute


# Import lists of combinations of the long titles
list_eu_ictrp_long = pickle.load( open( "../results/Pickles/list_eu_ictrp_long_titles.pickle", "rb" ) )

list_us_eu_long = pickle.load( open( "../results/Pickles/list_us_eu_long_titles.pickle", "rb" ) )

list_us_ictrp_long = pickle.load( open( "../results/Pickles/list_us_ictrp_long_titles.pickle", "rb" ) )


# Final long titles list
list_long_titles = delayed(list_eu_ictrp_long + list_us_eu_long + list_us_ictrp_long)

list_long_titles.compute()


# Final long titles dataframe
df_all_long_titles = pd.DataFrame(list_long_titles.compute(), columns=['id1_id2', 'indicator1_indicator2', 'longtitle1_longtitle2', 'similarity'])

df_all_long_titles.to_csv('../results/long_titles.csv', sep='|')

with open('../results/Pickles/df_all_long_titles.pickle', 'wb') as f:
   pickle.dump(df_all_long_titles, f)