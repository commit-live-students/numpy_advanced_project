import pandas as pd
def get_toss_win_count(team) :
    team=team.decode('ASCII')
    df =pd.read_csv('data/ipl_matches_small.csv')
    facedDel=df[(df['toss_winner']==team)]
    #print(len(facedDel))
    return len(facedDel.match_code.unique())
print(get_toss_win_count(b'Mumbai Indians'))
print('Hii')






