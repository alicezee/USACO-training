"""
LANG: PYTHON3
TASK: barn1
"""

fin = open("barn1.in", "r")     
fout = open("barn1.out", "w")

line = fin.readline().strip().split()
m = int(line[0])
s = int(line[1])
c = int(line[2])
stalls = []
occupied = fin.read().strip().split()
occupied = map(int, occupied)
occupied = sorted(occupied)

empty = 0
empties = []
for j in range(1, len(occupied)):
    empties.append(occupied[j] - occupied[j-1] - 1)

empties = sorted(empties, reverse=True)

noBoard = 0
cnt = 0
for k in range(len(empties)):
    if cnt == m-1:
        break
    noBoard += empties[k]
    cnt += 1


fout.write(str(occupied[-1]+1 - occupied[0] - noBoard) + "\n")