import numpy as np
import re

f = open("./Input/Day9.dat")

def update(H,T):
    diff = H-T
    if max(abs(diff))==1:
        return (H,T)
    else:
        if np.min(abs(diff))==0:  
            T = (T+(0.5*diff)).astype(int)
        else:
            T = (T+np.clip(diff,-1,1)).astype(int)
    return(H,T)

def update_many(pos):
    for i in range(pos.shape[0]-1):
        H = pos[i]
        T = pos[i+1]
        pos[i],pos[i+1]=update(pos[i],pos[i+1])
    return pos

def part1():
    H_pos = np.array((0,0))
    T_pos = np.array((0,0))

    Tposs=[]
    for line in f:
        n_step = int(line.split()[1])
        dirn = line.split()[0]

        if dirn=='U':
            dpos = np.array((0,1))
        elif dirn=='D':
            dpos = np.array((0,-1))
        elif dirn=='L':
            dpos = np.array((-1,0))
        elif dirn=='R':
            dpos = np.array((1,0))
            
        for i in range(n_step):
            H_pos += dpos
            H_pos,T_pos = update(H_pos,T_pos)

            Tposs.append("%s%s"%(T_pos[0],T_pos[1]))
    print(len(set(Tposs)))

def part2():
    pos = np.zeros((10,2))
    tposs = []
    for line in f:
        n_step = int(line.split()[1])
        dirn = line.split()[0]

        if dirn=='U':
            dpos = np.array([0,1])
        elif dirn=='D':
            dpos = np.array([0,-1])
        elif dirn=='L':
            dpos = np.array([-1,0])
        elif dirn=='R':
            dpos = np.array([1,0])
        for j in range(n_step):
            pos[0] += dpos 
            pos = update_many(pos)

            tposs.append("%s%s"%(pos[-1][0],pos[-1][1]))
    print(len(set(tposs)))

part2()
      
    
    
