import pandas as pd
import numpy as np

def get_all_sixes_filter():
    ipl_data=pd.read_csv('./data/ipl_matches_small.csv')
    six_or_not=np.array(ipl_data['runs']==6)
    return six_or_not
ipl_data=get_all_sixes_filter()
type(ipl_data)

