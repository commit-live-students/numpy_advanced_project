#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=0, delimiter=",")


#Your Solution
import pandas as pd
df= pd.DataFrame(ipl_matches_array)
df.columns = df.loc[0,:]
dfnew = df.drop(0)
def get_all_sixes_filter():
    new= np.array(dfnew['runs'])
    newarray = new.astype(np.int)
    return (newarray==6)
