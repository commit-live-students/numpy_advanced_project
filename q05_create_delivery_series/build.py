import pandas as pd
import numpy as np

def create_delivery_series() :
   # team=team.decode('ASCII')
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

    #ipl_matches_array =pd.read_csv('data/ipl_matches_small.csv')
    s1=pd.Series(ipl_matches_array[:,11])
    #expected_filter = (ipl_matches_array[:, 16] == 6)
    print(type(s1))
    #&(df['toss_decision']!='bat')
    return s1

print(create_delivery_series())


