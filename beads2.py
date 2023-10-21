"""
LANG: PYTHON3
TASK: beads
"""

fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')

length = int(fin.readline())
bracelet = fin.readline().strip()
greater = 0
loop = bracelet + bracelet
loopLength = length*2
start = 0
prev = 0
next = 0
exit = False

for l in range(length):
    if loop[l] != "w":
        start = l
        break

while start <= length:
    prev = start
    total = 0
    colorchange = 0
    while loop[prev-1] =="w" and prev > 0:
        prev -= 1
    for j in range(start+1, loopLength):
        if loop[j] != loop[start] and loop[j] != "w" and colorchange == 0:
            next = j
            colorchange = 1
        elif loop[j] == loop[start] and colorchange == 1:
            break
        if j == length-1 and colorchange ==0:
            j += 1
            exit = True
            break

    total = j - prev
    if total > greater:
        greater = total
    start = next
    if exit:
        start = length+1



fout.write(str(greater) + "\n")
fout.close()
