#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(player):

    var=list()
    count=-1
    for pla in ipl_matches_array[:,20]:
        count+=1
        if(pla==player):
            var.append(ipl_matches_array[count,11])


    return np.array(var)


print get_wicket_delivery_numbers_array("ST Jayasuriya")
