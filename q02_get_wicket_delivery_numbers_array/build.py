import pandas as pd
import numpy as np
def get_wicket_delivery_numbers_array(batsman):
    batsman=batsman.decode('ASCII')
    df =pd.read_csv('data/ipl_matches_small.csv')
   # print(df.head())
    players=[]
    player_out=df[(df['player_out']==batsman)]['delivery']
    for x in player_out :
        players.append(str(x).encode('ASCII'))
        #teams.add(x.encode('ASCII'))
    print(players)
    return np.array(players)

print(get_wicket_delivery_numbers_array(b'ST Jayasuriya'))


