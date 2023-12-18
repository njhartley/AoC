import numpy as np
from typing import List, Tuple
from functools import cache

# Open the file and read the lines into a list
lines: List[str] = open("./Input/Day12.txt").read().splitlines()
n_line = len(lines)


def hash_count(string):
    sets = string.replace('.',' ').split()
    return np.array([len(i) for i in sets])

#@cache
def count_arrangements(conditions, rules):
    print(conditions,rules)
    if not rules:
        if not '#' in conditions:
            print("Adding 1")
        return 0 if "#" in conditions else 1
    if not conditions:
        if not rules:
            print("Adding 1")
        return 1 if not rules else 0

    result = 0

    if conditions[0] in ".?":
        #print("Case 1")
        result += count_arrangements(conditions[1:], rules)
    if conditions[0] in "#?":   
        if (
            rules[0] <= len(conditions)
            and "." not in conditions[: rules[0]]
            and (rules[0] == len(conditions) or conditions[rules[0]] != "#")
        ):
            #print("Case 3")
            ## everything after first block
            result += count_arrangements(conditions[rules[0] + 1 :], rules[1:])
        else:
            pass
            #print("Case 2")

    return result

solution1 = 0
solution2 = 0

for j,line in enumerate(lines):  
    dat,num = line.split()
    num = eval(num)
    solution1 += count_arrangements(dat,num)
    break

##    dat_2 = '?'.join(dat*5)
##    num_2 = 5*num
##    solution2 += count_arrangements(dat_2,num_2)
    
print(solution1)
##print(solution2)


    

    
    
