from itertools import permutations
def minus(x,n): #user defined function to calculate 1-1 = n
	if x == 1:
		return n
	return x-1

inp = []
with open("input.txt") as f:    #opening input.txt file
	n = int(f.readline())
	for i in range(n):    
		inp.append(int(f.readline().strip()))   #removing white spaces

output = []
for i in inp:
	f = open("output.txt","a")  #opening output.txt file
	lis = []
	for j in range(i-1):    #creating list of i-1 elements to create permutation
		lis.append(j+1)
	
	permutation = list(permutations(lis))   #getting permutation of lis
	permutation = [list(j) for j in permutation]    #converting each permutation into list
	for perm in permutation:	#going through each permutation
		outcome = []
		outcome.append([i]+perm)	#adding first line
		for j in range(i-1):	#iterating i-1 times
			row = []
			for k in range(i):	#iterating i times
				row.append(minus(outcome[j][k],i))	#minus from previous row's k'th element and add it to new row

			outcome.append(row)	#append new row to outcome
		f.write(str(outcome)+"\n")	#write output to output.txt file
		