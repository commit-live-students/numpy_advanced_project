
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def create_delivery_series():
    df = pd.Series(ipl_matches_array[:, 11])
    return df
create_delivery_series()


