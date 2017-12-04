#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_toss_win_count(team):
    u={}
    c=0
    for i in ipl_matches_array[:,[0,5]]:
        u[i[0]]=i[1]
    for j in u.values():
        if j==team:
            c=c+1
    return c
