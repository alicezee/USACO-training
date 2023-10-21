"""
LANG: PYTHON3
TASK: milk3
"""
import math

vis = [[[0 for x in range(21)] for y in range(21)] for z in range(21)]

def mm(a,b,c):
    if vis[a][b][c] == 1:
        return
    vis[a][b][c] = 1
    if a == 0:
        possible.append(c)
    #a -> b
    x = min(a,maxb - b)
    mm(a-x, b+x, c)
    # a -> c
    x = min(a, maxc - c)
    mm(a - x, b, c + x)
    # b -> a
    x = min(b, maxa - a)
    mm(a + x, b - x, c)
    # b -> c
    x = min(b, maxc - c)
    mm(a, b - x, c + x)
    # c -> a
    x = min(c, maxa - a)
    mm(a + x, b, c - x)
    # c -> b
    x = min(c, maxb - b)
    mm(a, b + x, c - x)

fin = open("milk3.in", "r")
fout = open("milk3.out", "w")

maxa, maxb, maxc = map(int, fin.readline().strip().split())

possible = []

mm(0, 0, maxc)

possible = sorted(possible)

if len(possible) == 1:
    fout.write(str(possible[0]))

for i in range(0, len(possible)):
    fout.write(str(possible[i]))
    if i != len(possible)-1:
        fout.write(" ")
    else:
        fout.write("\n")









