"""
LANG: PYTHON3
TASK: sort3
"""

def swap(list, idx1, idx2):
    tVar = list[idx2]
    list[idx2] = list[idx1]
    list[idx1] = tVar
    return list


fin = open("sort3.in", "r")         #open input/output files
fout = open("sort3.out", "w")

lines = int(fin.readline().strip())     #read N
sequence = []       #store sequence

for i in range(lines):      #read in sequence
    sequence.append(int(fin.readline().strip()))

ones = sequence.count(1)        #count the number of 1s in the sequence
twos = sequence.count(2)        #count the number of 2s in the sequence
threes = sequence.count(3)      #count the number of 3s in the sequence
cnt = 0

for j in range(ones):       #iterate through the first elements that are supposed to be 1
    if sequence[j] != 1:        #if it is not 1, it needs to be swapped
        if sequence[j] == 2:    #if the element is 2
            if 1 not in sequence[ones:ones+twos]:       #if there is no 1 in the range that the elements are supposed to be 2
                sequence = swap(sequence, j, sequence[ones + twos:ones + twos + threes].index(1) + ones + twos)     #search for 1 in the range where the elements are supposed to be 3

            else:       #there is one or more 1s in the 2's region
                sequence = swap(sequence, j, sequence[ones:ones+twos].index(1)+ones)

        else:       #if the element is 3
            if 1 not in sequence[ones + twos:ones + twos + threes]:     #search in the threes region
                sequence = swap(sequence, j, sequence[ones:ones + twos].index(1) + ones)

            else:       #search in the twos region
                sequence = swap(sequence, j, sequence[ones + twos:ones + twos + threes].index(1) + ones + twos)

        cnt += 1        #number of swaps +1

for k in range(ones, ones + twos):      #iterate through the elements that are supposed to be 2s
    if sequence[k] == 3:        #since all 1s are in its right place, we only need to check for 3s
        sequence = swap(sequence, j, sequence[ones + twos :ones + twos + threes].index(2) + ones + twos)
        cnt += 1

fout.write(str(cnt) + "\n")     #output

