import numpy as np

f = open("./Input/Day10.dat")

output = np.zeros((40,6),dtype=str)

def checkt(t,x,output):
    sprite_pos = x
    draw_pos = int((t-1)%40)
    draw_row = int(np.floor((t-1)/40))

    try:
        if abs(sprite_pos-draw_pos)<2:
            output[draw_pos,draw_row]='0'
        else:
            output[draw_pos,draw_row]='-'
    except:
        pass
    
    if (t+20)%40==0:
        return t*x
    else:
        return 0

X=1
t=1
run_tot = checkt(t,X,output)

for line in f:
    if line[:4]=="noop":
        t += 1
        run_tot += checkt(t,X,output)
        
        
    elif line[:4]=="addx":
        t += 1
        run_tot += checkt(t,X,output)
        
        t += 1
        X += int(line.split()[1])
        run_tot += checkt(t,X,output)
        
print(run_tot)
for  i in range(8):
    print(output[5*i:5*(i+1)].T)
    print('\n')
