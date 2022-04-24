inp = []
with open("paytminp.txt") as f:
    n = int(f.readline())
    for i in range(n):
        inp.append(f.readline().strip())
inpset = []
for i in inp:
    x = [int(j) for j in i[1:-1].split(',')]
    inpset.append(x)

output = []
for lis in inpset:
    f = open("paytmout.txt","a")
    minp = max(lis)
    maxp = 0
    mind = 0
    for i in range(len(lis)):
        if lis[i] < minp:
            minp = lis[i]
    
        elif lis[i] - minp > maxp:
            maxp = lis[i] - minp
            mind = i

    hr = (570 + (mind*10) + 10) // 60
    if hr > 12:
        hr = hr - 12
    
    min = (570 + (mind*10) + 10) % 60
    time = str(hr) + '.' + str(min)
    output.append([maxp,time])
    f.write(str([maxp,time])+"\n")
    f.close()
