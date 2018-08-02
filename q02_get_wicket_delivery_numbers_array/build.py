# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    a=ipl_matches_array
    q=[]
    p=[]
    for i in range(len(a)):
        b=tuple((a[i][11],a[i][20]))
        q.append(b)
    for i in q:
        if i[1]==batsman:
            p.append(i[0])
    return np.array(p)
c=get_wicket_delivery_numbers_array(b'ST Jayasuriya')
c



