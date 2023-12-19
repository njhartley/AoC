import numpy as np
from typing import List, Tuple
from collections import Counter

# Open the file and read the lines into a list
lines: List[str] = open("./Input/Day7.txt").read().splitlines()

def val(char):
    try:
        return int(char)
    except:
        if char=='A':
            return 14
        elif char=='K':
            return 13
        elif char=='Q':
            return 12
        elif char=='J':
            return 1
        elif char=='T':
            return 10
        else:
            print(char)

hands=[]
keys = np.zeros(len(lines))
bids = np.zeros(len(lines))


## Assign numerical value to each hand
for i,line in enumerate(lines):
    hand,bid =line.split()

    ## Count and remove jokers
    n_J = hand.count('J')
    hand_ana = hand.replace('J',"")

    ## Count cards in remaining hand
    try:
        c = Counter(hand_ana)        
        n_max = (c.most_common(1)[0][1] - 1) + n_J
    except:
        n_max = 4

    if n_max==2:
        if c.most_common(2)[1][1]==2:
            n_max = 2.5
    elif n_max==1:
        if c.most_common(2)[1][1]==2:
            n_max = 1.5            

    hands.append(hand)
    key = n_max*1e14 + 1e8*val(hand[0]) + 1e6*val(hand[1]) + 1e4*val(hand[2]) + 1e2*val(hand[3]) + val(hand[4])
    keys[i] = key
    bids[i] = int(bid)

args = np.argsort(keys)
Nt = len(keys)-1

hands_sort = [hands[i] for i in args]
keys_sort = [keys[i] for i in args]
bids_sort = [bids[i] for i in args]
rating = np.arange(1,1+len(bids),1)

for i in range(10):
    print(i+1,hands_sort[Nt-i],bids_sort[Nt-i])

print(np.sum( rating * bids_sort))
    

    


