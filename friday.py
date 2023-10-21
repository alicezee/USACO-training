"""
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

years = int(fin.readline())
year = 1900
DayOfWeek = [0, 0, 0, 0, 0, 0, 0]
year_start = 1
leap = [13, 44, 73, 104, 134, 165, 195, 226, 257, 287, 318, 348]
nonleap = [13, 44, 72, 103, 133, 164, 194, 225, 256, 286, 317, 347]
for i in range(years):
    for j in range(12):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 != 0:
                    idx = ((nonleap[j] + year_start) % 7) - 1
                else:
                    idx = ((leap[j] + year_start) % 7) - 1
            else:
                idx = ((leap[j] + year_start) % 7) - 1
        else:
            idx = ((nonleap[j] + year_start) % 7) -1
        if idx == -1:
            idx = 6
        DayOfWeek[idx] += 1
    year += 1

    year_start = ((18 % 7) + idx) % 7 + 1
fout.write (str(DayOfWeek[6]) + ' ' + str(DayOfWeek[0]) + ' ' + str(DayOfWeek[1]) + ' ' + str(DayOfWeek[2]) + ' ' + str(DayOfWeek[3]) + ' ' + str(DayOfWeek[4]) + ' ' + str(DayOfWeek[5]) + '\n')
fout.close()
