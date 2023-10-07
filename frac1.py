"""
LANG: PYTHON3
TASK: frac1
"""

fin = open("frac1.in", "r")     #open input/output files
fout = open("frac1.out", "w")

N = int(fin.readline().strip())     #read N

fout.write("0/1\n")     #output 0 (first fraction)
fracDec = []        #store fraction and deciaml value
dec = []        #store decimal value only

for i in range(2, N+1):         #iterate denominator values
    for j in range(1, i):       #iterate numerator values
        divident = j/i          #calculate deciaml value
        if divident in dec:     #if there is already a fraction that has the same value ex: 1/2 == 2/4, only store 1/2
            continue
        else:
            dec.append(divident)
            fracDec.append([divident, i, j])        #decimal as first element for sorting

fracDec.sort()      #sort from least to greatest

for k in fracDec:       #output fractions
    fout.write(str(k[2]) + "/" + str(k[1]) + "\n")

fout.write("1/1\n")     #output 1 (last fraction)
