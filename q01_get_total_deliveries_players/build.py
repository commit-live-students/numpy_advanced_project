# Default imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution
def get_total_deliveries_played(batsman='ST Jayasuriya'):
    df = DataFrame(ipl_matches_array[:,13], columns=['Batsman'])

    df['count'] = 1

    on_bat = df.pivot_table('count', aggfunc=np.sum, index='Batsman')
    Jay = on_bat.loc[batsman].item()

    return Jay

print get_total_deliveries_played('ST Jayasuriya')
