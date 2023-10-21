"""
LANG: PYTHON3
TASK: gift1
"""
import math

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

name = []
money = []

x = int(fin.readline())
for i in range(x):
    name.append(fin.readline().replace('\n', ''))
    money.append(0)

for j in range(x):
    p = name.index(fin.readline().replace('\n', ''))
    gifting = fin.readline().split()
    
    if gifting[0] != "0" or gifting[1] != "0":
        money[p] = money[p] - int(gifting[0]) + (int(gifting[0]) % int(gifting[1]))
        mper = int(gifting[0]) / int(gifting[1])
        mper = math.floor(mper)

    for k in range(int(gifting[1])):
        money[name.index(fin.readline().replace('\n', ''))] += mper

for l in range(x):
    fout.write(name[l] + " " + str(money[l]) + '\n')

fout.close()
