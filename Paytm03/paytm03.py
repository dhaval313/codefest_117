inp = []
with open("input.txt") as f: #opening input file
    n = int(f.readline())
    for i in range(n):
        inp.append(f.readline().strip())    #removing white spaces
inpset = []
for i in inp:
    x = [int(j) for j in i[1:-1].split(',')]    #converting input to list
    inpset.append(x)

for lis in inpset:  
    f = open("output.txt","a")  #opening output file
    minp = max(lis)
    maxp = 0    #to store maximum profit
    mind = 0    #to store index of selling price
    for i in range(len(lis)):
        if lis[i] < minp:   #if i is smaller than minp, then it replaces minp
            minp = lis[i]
    
        elif lis[i] - minp > maxp:  #if i - minimum element is greather than maximum profit then update maxp and mind
            maxp = lis[i] - minp
            mind = i

    hr = (570 + (mind*10)) // 60   #addint 570 mins (9:30 hours) to selling time, dividing it by 60 and storing floor value
    if hr > 12:
        hr = hr - 12    #convert to 12hr format if it's over hr is over 12
    
    min = (570 + (mind*10)) % 60   #storing minutes 
    time = str(hr) + '.' + str(min) #formating time

    f.write(str([maxp,time])+"\n")  #writing in output.txt file
    f.close()
