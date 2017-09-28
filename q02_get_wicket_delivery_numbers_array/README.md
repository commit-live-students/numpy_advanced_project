## Get the array of all delivery numbers when a given player got out
 

Write a function to get the number of deliveries 
faced by a batsman before got out with following specifications.

**The function should**
- Be named `get_wicket_delivery_numbers_array`
- Accept one mandatory parameter named `player`. The input type is `str`
- Work on the previously created `ipl_matches_array` object. We have already imported that for you
- Should return a numpy array of all (non unique) delivery numbers when a player got out