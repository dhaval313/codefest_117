from collections import defaultdict

inp = [] 
with open("input.txt") as f: #opening input file
    n = int(f.readline())
    for i in range(n):
        inp.append(f.readline().strip()) #to remove extra spaces
inpset = []
for i in inp:
    x = [int(j) for j in i[1:-1].split(',')] #converting string into list
    inpset.append(set(x)) #converting list into set to remove duplicates

count = 1
outdic = defaultdict(lambda: None) 
output = []

for i in range(len(inpset)):
    outdic[sum(inpset[i])] = i + 1 #calculates total of all unique value in sets iteratively

for i in sorted(outdic.keys()):
    output.append(outdic[i]) #sorting data by time taken
    output.append(i)

f = open("output.txt","w")
f.write(str(output)) #writing output in output.txt
print(output)
