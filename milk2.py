"""
LANG: PYTHON3
TASK: milk2
"""
def myFunc(e):
    return e["start"]

def milk(time, num):
    time.sort(key = myFunc)
    continuous = time[0]["end"] - time[0]["start"]
    idle = 0
    max_c = continuous
    max_i = idle
    start_idx = time[0]["start"]
    end_idx = time[0]["end"]
    for j in range(1,num):
        if time[j]["end"] < end_idx:
            continue
        if time[j]["start"] <= end_idx:
            end_idx = time[j]["end"]
        else:
            continuous = end_idx - start_idx
            idle = time[j]["start"] - end_idx
            max_c = max(max_c, continuous)
            max_i = max(max_i, idle)
            start_idx = time[j]["start"]
            end_idx = time[j]["end"]
    return max_c, max_i

fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

num_of_farmers = int(fin.readline().strip())
farmers = []

for i in range(num_of_farmers):
    line = fin.readline().strip().split()
    farmers.append({"start" : int(line[0]), "end" : int(line[1])})

continuous, idle = milk(farmers, num_of_farmers)

fout.write(str(continuous) + " " + str(idle) + "\n")
fout.close()