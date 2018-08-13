#Default Imports
import numpy as np
import pandas as pd
from pandas import Series,DataFrame
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(player_Out='SR Tendulkar'):
    data_02= ipl_matches_array[:,[11,20]]
    df = pd.DataFrame(data_02, columns=['Deliveries', 'Player_Out'])

    df[df == ''] = 'Not_Out'
    l = df.loc[df['Player_Out'] == player_Out, 'Deliveries']
    w = l.tolist()
    final = np.array(w)
    #pdf = df.set_index('Player_Out')
    #on_bat_Sach = pdf.loc['SR Tendulkar']
    #Sach_Ten = on_bat_Sach.values.tolist()
    #sach_out = np.array(['7.6', '12.2', '1.5'])

    return final


print get_wicket_delivery_numbers_array('SR Tendulkar')
