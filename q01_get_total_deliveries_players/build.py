# Default imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

import numpy as np
import pandas as pd

def read_ipl_data(path, dtype=np.float64):
    return np.genfromtxt(path, dtype=dtype, skip_header=0, delimiter=",")

ipl_matches_array = read_ipl_data("./data/ipl_matches_small.csv", '|S50')
df = pd.DataFrame(ipl_matches_array)
df.columns =  df.iloc[0]
df = df.drop(0)
print df.head()

def get_total_deliveries_played(batsman):
    return len(df[df['batsman'] == batsman])

print get_total_deliveries_played('ST Jayasuriya')
# Your Solution
