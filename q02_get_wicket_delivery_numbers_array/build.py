#Default Imports
import numpy as np

from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_wicket_delivery_numbers_array(player):
    player_out_delivery = ipl_matches_array[ipl_matches_array[:,20] == player][:,11]
    return player_out_delivery

#print 'STJ:{0}'.format(get_wicket_delivery_numbers_array('ST Jayasuriya'))
#print 'Yuvraj:{0}'.format(get_wicket_delivery_numbers_array('Yuvraj Singh'))
#print '10dulkar:{0}'.format(get_wicket_delivery_numbers_array('SR Tendulkar'))
