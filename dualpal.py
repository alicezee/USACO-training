"""
LANG: PYTHON3
TASK: dualpal
"""
import math

def convertBase(num, base):
    answer = num
    quotient = 0
    converted = ''
    convertedRef = ''
    while answer != 0:
        quotient = answer % base
        answer = math.floor(answer / base)
        converted = str(quotient) + converted
        convertedRef = convertedRef + str(quotient)

    return converted, convertedRef

if __name__ == "__main__":
    fin = open("dualpal.in", "r")
    fout = open("dualpal.out", "w")

    input = fin.readline().strip().split()
    N = int(input[0])
    S = int(input[1])
    i = S+1
    numOfnum = 0
    while i > S:
        bucket = 0
        for j in range(2, 11):
            converted, convertedRef = convertBase(i, j)
            if converted == convertedRef:
                bucket += 1

        if bucket >= 2:
            fout.write(str(i) + "\n")
            numOfnum += 1

        if numOfnum == N:
            break

        i += 1
