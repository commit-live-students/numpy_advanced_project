#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=0, delimiter=",")

#Your Solution
df= pd.DataFrame(ipl_matches_array)
df.columns = df.loc[0,:]
dfnew = df.drop(0)
def create_runs_series(code):
   return dfnew[dfnew['match_code']== str(code)]['runs']
