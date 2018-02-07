#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code='392203'):
    df = pd.DataFrame(ipl_matches_array[:,[0,11,16]], columns=['match','deliveries', 'runs'])
    l = df.loc[df['match'] == match_code, ['deliveries', 'runs']]

    s = pd.Series(l['runs'].values, index=l['deliveries'])

    return s

print create_runs_series('392203')
