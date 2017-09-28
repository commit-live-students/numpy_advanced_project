# Numpy Advanced

## What have we learnt so far 
We have seen how to manipulate a dataset using the following tools of the numpy library:

- Indexing and Selection
- Slicing
- Filters
- Pandas

## Why solve this assignment?

By the completing this Assignment
you will get hands-on practice with advanced techniques like creating, 
manipulating and accessing the information needed from data structures.

## About the dataset

This assignment continues with the same IPL dataset we have been using. 
Let's get our hands dirty!


---
**Tip**:

A good way to get the integer indexes for columns is to enumerate() them
```
cols = ['match_code', 'date', 'city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner','win_type',
        'win_margin', 'inning', 'delivery', 'batting_team', 'batsman', 'non_striker', 'bowler', 'runs', 'extras',
        'total', 'extras_type', 'player_out', 'wicket_kind', 'wicket_fielders']
list(enumerate(cols))
```