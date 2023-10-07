"""
LANG: PYTHON3
TASK: ariprog
"""
import math

def check(s, d):
    for k in range(n):
        val = s + d * k
        if val not in bisqr:        #the kth element is not in bisqr
            return False
    return True     #all elements of this sequence is in bisqr

fin = open('ariprog.in', 'r')      #open input/output files
fout = open('ariprog.out', 'w')

n = int(fin.readline().strip())     #read in N
m = int(fin.readline().strip())     #read in M

bisqr = []      #store all bisquares
ans = []        #store all answer pairs

for p in range(0, m+1):         #find all bisquares in range 0< bisquare < (p^2 + q^2)
    for q in range(0, m+1):
        bisqr.append(p**2 + q**2)


for i in range(2*m*m):      #iterate [0,p^2+q^2)
    for j in range(1, math.ceil((2*m*m-i)/(n-1)) + 1):      #iterate possible differences
        if check(i, j):     #if the first n element of the sequence is in bisqr
            ans.append([j, i])

ans.sort()      #smallest starting number first

if ans == []:       #no sequence is found
    fout.write("NONE\n")

else:
    for l in ans:
        fout.write(str(l[1]) + " " + str(l[0]) + "\n")


