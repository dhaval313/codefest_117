inp = []
with open("mayurinp.txt") as f:
    n = int(f.readline())
    for i in range(n):
        temp = []
        for j in range(3    ):
            temp.append(f.readline().strip())
        inp.append(temp)

inpset = []
for i in inp:
    temp = []
    for k in i:
        x = [int(j) for j in k[1:-1].split(',')]
        temp.append(x)
    inpset.append(temp)
    
output = []
for i in inpset:
    lt = len(i[0])
    ld = len(i[1])
    t = d = 0
    flag = False
    for j in i[2]:
        if t < lt and j == i[0][t]:
            t += 1

        elif d < ld and j == i[1][d]:
            d += 1

        else:
            output.append("Invalid")
            flag = True
            break
        
    if not flag:
        output.append("Valid")
        

for i in output:
    with open("mayurout.txt","a") as f:
        f.write(i+"\n")
