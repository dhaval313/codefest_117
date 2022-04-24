inp = []
with open("input.txt") as f: #opening input file
    n = int(f.readline())
    for i in range(n):
        temp = []
        for j in range(3):
            temp.append(f.readline().strip()) #making list of 3 lists
        inp.append(temp)

inpset = []
for i in inp:
    temp = []
    for k in i:
        x = [int(j) for j in k[1:-1].split(',')]    #converting string into lists
        temp.append(x)
    inpset.append(temp)
    
output = []
for i in inpset:    #going through input list
    lt = len(i[0])  
    ld = len(i[1])
    t = d = 0   #initializing counters for takeout and dinein list
    flag = False
    for j in i[2]:
        if t < lt and j == i[0][t]: #checking if served order is of takeout
            t += 1

        elif d < ld and j == i[1][d]:   #checking if served order is of dinein
            d += 1

        else:   #if it's of neither then output is "invalid"
            output.append("Invalid")
            flag = True
            break
        
    if not flag:    #if the flag is still false then it means it's "valid"
        output.append("Valid")
        

for i in output:
    with open("output.txt","a") as f:
        f.write(i+"\n") #writing output in output.txt file
