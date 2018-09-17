#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    
    delivery = ipl_matches_array[:,11]# delievery column which has to be given in op is considered as main dataset
    
    
    playerout = ipl_matches_array[:,20]==batsman # [create filter: batsman] accesssing the column playerout 
    
   
    deliveries_out=delivery[playerout].astype(bytes)  #apply the filter in the main data(deliveries to get the values)
    
    return deliveries_out

get_wicket_delivery_numbers_array(b'SR Tendulkar')


]




