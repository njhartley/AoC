import numpy as np
import re

f = open("./Day6 Input.dat")

dat = f.readline()
#dat = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"

length = 14

for a in range(len(dat)):
    l1 = dat[a:a+length]
    s1 = set(l1)
    if len(l1)==len(s1):
        print(a+length)
        print(l1)
        print(s1)
        break
    
