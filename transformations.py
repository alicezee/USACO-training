"""
LANG: PYTHON3
TASK: transform
"""

def ninety(before, after, size):
    changed = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            changed[j][size-1-i] = before[i][j]
    if after == changed:
        return True
    else:
        return False

def one_eighty(before, after, size):
    changed = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            changed[size-1-i][size-1-j] = before[i][j]
    if after == changed:
        return True
    else:
        return False

def two_seventy(before, after, size):
    changed = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            changed[size-1-j][i] = before[i][j]
    if after == changed:
        return True
    else:
        return False

def reflection(before, after, size):
    changed = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            changed[i][size-j-1] = before[i][j]
    if after == changed:
        return True
    else:
        return False

def combination(before, after, size):
    changed = [[0 for x in range(size)] for y in range(size)]
    for i in range(size):
        for j in range(size):
            changed[i][size - j - 1] = before[i][j]
    if ninety(changed, after, size):
        return True
    elif one_eighty(changed, after, size):
        return True
    elif two_seventy(changed, after, size):
        return True
    else:
        return False

def no_change(before, after):
    if before == after:
        return True
    else:
        return False


if __name__ == "__main__":
    fin = open('transform.in', 'r')
    fout = open('transform.out', 'w')

    size = int(fin.readline().strip())
    original = [[0 for x in range(size)] for y in range(size)]
    trans = [[0 for x in range(size)] for y in range(size)]


    for i in range(size):
        row = fin.readline().strip()
        for j in range(size):
            original[i][j] = row[j]

    for i in range(size):
        row = fin.readline().strip()
        for j in range(size):
            trans[i][j] = row[j]


    if ninety(original, trans, size):
        fout.write("1\n")
    elif one_eighty(original, trans, size):
        fout.write("2\n")
    elif two_seventy(original,trans,size):
        fout.write("3\n")
    elif reflection(original, trans, size):
        fout.write("4\n")
    elif combination(original, trans, size):
        fout.write("5\n")
    elif no_change(original, trans):
        fout.write("6\n")
    else:
        fout.write("7\n")