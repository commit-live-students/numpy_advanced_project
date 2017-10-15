# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
player="ST Jayasuriya"
t1=[]
#Your Solution
def get_wicket_delivery_numbers_array(player):
    test=ipl_matches_array[1:,[11,20]]
    out=test[test[:,1]==player]
    ans=out[:,0]
    #print(test[:,1])
#     for i in test:
#         if (i[1]==player):
#             t1.append(i[0])
#         else:
#             continue
#         test=np.array(t1)
#         print(type(test))
    return(ans)



get_wicket_delivery_numbers_array(player)
