#%load q05_create_delivery_series/build.py
import pandas as pd
import numpy as np
path='./data/ipl_matches_small.csv'
def create_delivery_series():
    #df=pd.read_csv('./data/ipl_matches_small.csv')
    
    data=np.genfromtxt(path,delimiter=',',skip_header=1,dtype='|S20')
    delivery=pd.Series(data[:,11])
    
 
    return delivery

create_delivery_series()
  


