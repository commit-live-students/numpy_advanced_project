import pandas as pd

def get_toss_win_count(team):
    ipl_data=pd.read_csv('./data/ipl_matches_small.csv')
    toss_wins=ipl_data[ipl_data['toss_winner']==team]
    toss_wins_count=toss_wins['match_code'].nunique()
    return toss_wins_count
ipl_data=get_toss_win_count('Mumbai Indians')
ipl_data

