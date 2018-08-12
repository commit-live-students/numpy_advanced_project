#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution

def get_toss_win_count(team):
    count=0

    columntoss=ipl_matches_array[:,5]
    columnmatch=ipl_matches_array[:,0]

    #utoss=np.unique(columntoss)
    #umatch=np.unique(columnmatch)

    matchcodelist=list()
    temp=0
    for i in columnmatch:
        temp+=1
        if not(i in matchcodelist):

            matchcodelist.append(i)
            if columntoss[temp]==team:
                count+=1




    return count

#print get_toss_win_count("Mumbai Indians")
