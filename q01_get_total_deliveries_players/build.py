import pandas as pd
def get_total_deliveries_played(batsman) :
    batsman=batsman.decode('ASCII')
    df =pd.read_csv('data/ipl_matches_small.csv')
    facedDel=df[(df['batsman']==batsman)]
    #print(len(facedDel))
    return len(facedDel)
print(get_total_deliveries_played(b'SR Tendulkar'))


