#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=0, delimiter=",")


#Your Solution
import pandas as pd
df= pd.DataFrame(ipl_matches_array)
df.columns = df.loc[0,:]
dfnew = df.drop(0)
def get_toss_win_count(team):
    x = dfnew.groupby('match_code')['toss_winner'].value_counts()
    y = x.index
    z = np.array([i[1] for i in y])
    boolean = z == team
    return boolean.sum()
