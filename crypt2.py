"""
LANG: PYTHON3
TASK: crypt1
"""

def multiple(x):
    global cnt
    for i in numsInt:
        if len(x) < 5:
            x.append(i)

            if len(x) == 3:
                if x[2] == 0:
                    x.pop(2)
                    continue
            elif len(x) == 4:
                m1 = (x[2] * 100 + x[1] * 10 + x[0]) * x[3]
                if m1 > 999:
                    x.pop(3)
                    continue
                invalid = False
                for j in str(m1):
                    if j not in nums:
                        invalid = True
                        break
                if invalid:
                    x.pop(3)
                    continue
            elif len(x) == 5:
                m2 = (x[2] * 100 + x[1] * 10 + x[0]) * x[4]
                if m2 > 999:
                    x.pop(4)
                    continue
                invalid = False

                for j in str(m2):
                    if j not in nums:
                        invalid = True
                        break
                if invalid:
                    x.pop(4)
                    continue
                r = ((x[2] * 100 + x[1] * 10 + x[0]) * x[3]) + m2 * 10
                for k in str(r):
                    if k not in nums:
                        invalid = True
                        break
                if invalid:
                    x.pop(4)
                    continue
                cnt += 1
            multiple(x)
            x.pop(-1)
        else:
            break




fin = open("crypt1.in", "r")
fout = open("crypt1.out", "w")

numOfnums = int(fin.readline().strip())
nums = fin.readline().strip().split()
numsInt = list(map(int, nums))
cnt= 0
multiple([])
fout.write(str(cnt) + "\n")


