"""
LANG: PYTHON3
TASK: milk
"""

fin = open("milk.in", "r")
fout = open("milk.out", "w")

line = fin.readline().strip().split()
need = int(line[0])
numOfFarmers = int(line[1])
eachFarmer = []
totalCost = 0
for i in range(numOfFarmers):
    info = fin.readline().strip(). split()
    eachFarmer.append([int(info[0]), int(info[1])])
eachFarmer = sorted(eachFarmer)

for j in eachFarmer:
    if j[1] < need:
        totalCost += j[1] * j[0]
        need -= j[1]
    else:
        totalCost += j[0] * need
        break

fout.write(str(totalCost) + "\n")


