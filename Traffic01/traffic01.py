inp = []
with open("trainp.txt") as f:
    n = int(f.readline())
    for i in range(n):
        inp.append(f.readline().strip())
inpset = []
for i in inp:
    x = [int(j) for j in i[1:-1].split(',')]
    inpset.append(set(x))

count = 1
output = []
for i in inpset:
    output.append(count)
    output.append(sum(set(i)))
    count += 1

f = open("traout.txt","w")
f.write(str(output))
