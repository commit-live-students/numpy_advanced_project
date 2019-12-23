import pandas as pd
import numpy as np

def create_runs_series(match_code) :
    match_code=match_code.decode('ASCII')
    #ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    ipl_matches_arrays=[]
    ipl_match_delivery=[]
    ipl_match_runs=[]
    #for data in ipl_matches_array :
        #print(data[0])
        #if(data[0]==match_code):
            #ipl_match_delivery.append(data[11:12])
            #ipl_match_runs.append(data[16:17])
    ipl_matches_array_new =pd.read_csv('data/ipl_matches_small.csv')
    #ipl_matches_arrays=[ipl_matches_array[:,0:1],ipl_matches_array[:,11:12],ipl_matches_array[:,16:17]]
    #s1=pd.Series(ipl_matches_arrays,index=['match_code','delivery','runs'])
    #print(match_code)
    s1=ipl_matches_array_new[ipl_matches_array_new['match_code']==int(match_code)]
    #expected_filter =s1[(s1['match_code'] == match_code)]
    #print(s1['runs'])
    indexs=np.array(s1['delivery'])
    values=np.array(s1['runs'])
    s2=pd.Series(values,index=indexs)
    print(s2)
    #&(df['toss_decision']!='bat')
    return s2

print(create_runs_series(b'392203'))







