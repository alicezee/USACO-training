"""
LANG: PYTHON3
TASK: namenum
"""


def letter(serialNum, name):
    if len(serialNum) > 0:
        for i in range(3):
            name += gcodeTranslation[int(serialNum[0])][i]
            letter(serialNum[1:], (name + gcodeTranslation[int(serialNum[0])][i]))
    else:
        names.append(name)


if __name__ == "__main__":
    fin = open("namenum.in", 'r')
    fout = open("namenum.out", 'w')
    num = fin.readline().strip()
    names = []
    name = ""
    gcodeTranslation = [[], [], ["A", "B", "C"], ["D", "E", "F"], ["G","H", "I"], ["J", "K", "L"], ["M", "N", "O"], ["P", "R", "S"], ["T", "U", "V"], ["W", "X", "Y"]]
    letter(num, name)
    dictionary = open("dict.txt", "r")
    dictNames = []
    isFound = False
    for j in dictionary:
        j = j.strip()
        if len(j) == len(num):
            dictNames.append(j.strip())
    for i in names:
        if i in dictNames:
            fout.write(i + "\n")
            isFound = True
    if isFound ==False:
        fout.write("NONE\n")