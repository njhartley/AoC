import numpy as np

f = open("Day1.txt")

## Part 2
nums = ['one','two','three','four','five','six','seven','eight','nine']
nums2 = ['o1e','t2o','th3ee','fo4r','fi5e','s6x','se7en','ei8ht','ni9e']

def txt_replace(string):
    #print(string[:-1])
    j=0
    while j<=len(string):
        ana_string = string[:j]
        for i in range(9):
            if nums[i] in ana_string:
                string = string.replace(nums[i],nums2[i],1)
        j+=1

    #print(string[:-1])            
    return(string)

run_tot = 0

for line in f:
    ## Replace words with numbers
    line_2 = txt_replace(line)

    ## Convert to list of characters
    line_list = list(line_2)

    ## True/false - is character digit
    nums_list = [i.isdigit() for i in line_list]

    ## Where are the digits?
    xs = np.where(np.array(nums_list)==True)[0]

    ## First and last digit
    i1 = line_list[xs[0]]
    i2 = line_list[xs[-1]]

    ## Combine to number
    val = 10*int(i1) + int(i2)
    #nt(run_tot,val)
    #print(val)

    run_tot += val
print("Part 2 Answer: %s"%run_tot)
f.close()


 Part 1
f = open("Day1.txt")
run_tot = 0
for line in f:
    ## Convert to list of characters
    line_list = list(line)

    ## True/false - is character digit
    nums_list = [i.isdigit() for i in line_list]

    ## Where are the digits?
    xs = np.where(np.array(nums_list)==True)[0]

    ## First and last digit
    i1 = line_list[xs[0]]
    i2 = line_list[xs[-1]]

    ## Combine to number
    val = 10*int(i1) + int(i2)
    #print(run_tot,val)

    run_tot += val
print("Part 1 Answer: %s"%run_tot)



