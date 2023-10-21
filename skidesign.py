"""
LANG: PYTHON3
TASK: skidesign
"""

fin = open("skidesign.in", "r")
fout = open("skidesign.out", "w")

numOfHills = int(fin.readline().strip())
hills = list(map(int, fin.read().strip().split()))

hills = sorted(hills)
costs = []
for i in range(hills[-1]+1):
    isFound = False
    costs.append(0)
    for j in range(len(hills)):
        if hills[j] < i:
            costs[i] += (i - hills[j]) * (i - hills[j])
        elif hills[j] > i+17:
            costs[i] += (hills[j] - (i + 17)) * (hills[j] - (i + 17))


fout.write(str(min(costs)) + "\n")