"""
LANG: PYTHON3
TASK: ride
"""


def num(n):
    leng = len(n)
    mtp = 1
    for i in range(leng):
        if n[i] != '\n':
            mtp = mtp * (ord(n[i]) - 64)
    return mtp


fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
x = num(fin.readline())
y = num(fin.readline())
if x % 47 == y % 47:
    fout.write("GO" + '\n')
else:
    fout.write("STAY" + '\n')
fout.close()
