import numpy as np

f = open("./Input/Day2.txt")

## Part 2
run_tot=0
for line in f:
    ## Get game id
    idno = int(line.split(':')[0].split()[1])
    turns = line.strip().split(':')[1].split(';')
    #print(turns)
    
    ## RBG values
    vals = np.zeros((len(turns),3))

    ## Get ball number for each turn
    for i,turn in enumerate(turns):
        balls = turn.split(',')
        for ball in balls:
            if 'red' in ball:
                vals[i][0] = int(ball.split()[0])
            if 'green' in ball:
                vals[i][1] = int(ball.split()[0])
            if 'blue' in ball:
                vals[i][2] = int(ball.split()[0])
                
    ## Find max for each color
    games = np.max(vals,axis=0)

    power = games[0]*games[1]*games[2]
    run_tot += power

print(run_tot)

## Part 1
##run_tot=0
##for line in f:
##    ## Get game id
##    idno = int(line.split(':')[0].split()[1])
##    turns = line.strip().split(':')[1].split(';')
##    #print(turns)
##    
##    ## RBG values
##    vals = np.zeros((len(turns),3))
##
##    ## Get ball number for each turn
##    for i,turn in enumerate(turns):
##        balls = turn.split(',')
##        for ball in balls:
##            if 'red' in ball:
##                vals[i][0] = int(ball.split()[0])
##            if 'green' in ball:
##                vals[i][1] = int(ball.split()[0])
##            if 'blue' in ball:
##                vals[i][2] = int(ball.split()[0])
##    ## Find max for each color
##    games = np.max(vals,axis=0)
##
##    tf = games<=np.array([12,13,14])
##    #print(games)
##    
##    if tf.all():
##        run_tot += idno
##print(run_tot)
