import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def create_runs_series(m_code):
    a=ipl_matches_array[:,0]
    itemindex = np.where(a==m_code)
    ilst = list(itemindex)
    reqd_rows=ipl_matches_array[ilst]
    deliver = reqd_rows[:,11]
    runn = reqd_rows[:,16]
    s=pd.Series(runn,index=deliver)
    return s
