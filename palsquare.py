"""
LANG: PYTHON3
TASK: palsquare
"""
import math

def baseConversion(base, num):
    square = num * num
    answer = square
    numAnswer = num
    quotient = 0
    numQuotient = 0
    converted = ""
    convertedRef = ""
    convertedNum = ""
    while answer != 0:
        quotient = int(answer % base)
        answer = math.floor(answer/base)
        if quotient >= 10:    #base larger than 10
            converted = gNdex[quotient - 10] + converted
            convertedRef = convertedRef + gNdex[quotient - 10]
        else:
            converted = str(quotient) + converted
            convertedRef = convertedRef + str(quotient)

    while numAnswer != 0:
        numQuotient = int(numAnswer % base)
        numAnswer = math.floor(numAnswer/base)
        if numQuotient >= 10:
            convertedNum = gNdex[numQuotient - 10] + convertedNum
        else:
            convertedNum = str(numQuotient) + convertedNum
    return converted, convertedRef, convertedNum

def ifPalindromic(convertedSquare, convertedRef):
    if convertedSquare == convertedRef:
        return True
    else:
        return False

if __name__ == "__main__":
    fin = open("palsquare.in", "r")
    fout = open("palsquare.out", "w")

    base = int(fin.readline().strip())
    gNdex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    for i in range(1, 301):
        convertedSquare, convertedRef, convertedNum = baseConversion(base, i)

        if ifPalindromic(convertedSquare, convertedRef):
            fout.write(convertedNum + " " + convertedSquare + "\n")
