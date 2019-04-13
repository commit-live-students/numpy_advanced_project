# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def create_runs_series(match_code):
    match_code = int((match_code).decode('utf-8'))
    df = pd.read_csv('data/ipl_matches_small.csv')
    df2 = df.loc[(df['match_code']==match_code)]
    df_main = pd.DataFrame(index=df2['delivery'], columns=['runs'])
    for i in range(len(df2)):
        index = df2['delivery'][i]
        df_main['runs'][index] = df['runs'][i]
    return df_main.squeeze()
#int((b'392203').decode('utf-8'))
#type(create_runs_series(b'392203'))
#s = dfdf.squeeze()
#type(s)



