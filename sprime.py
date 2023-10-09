"""
LANG: PYTHON3
TASK: sprime
"""
import math

def recur(primes, zeros):       #recursion process to find all superprime ribs
    global length
    global ans
    if zeros > length:      #if the length of the number exceeds N, exit recursion
        return
    saves = []
    for i in primes:        #iterate through possible first digits of the number
        for j in range(1, 10, 2):       #add to the existing number
            isPrime = True
            num = i*10 + j
            for k in range(3, math.floor(math.sqrt(num))+ 1, 2):        #determine if number is prime
                if num%k == 0:          #not prime
                    isPrime = False
                    break

            if isPrime:         #is prime, append to possible answers
                saves.append(num)
                if zeros == length:
                    ans.append(num)

    recur(saves, zeros + 1)     #enter next stage



fin = open("sprime.in", "r")        #open input/output files
fout = open("sprime.out", "w")

length = int(fin.readline().strip())        #read in N

ans = []        #store superprime ribs (output)

if length == 1:         #if N == 1, the only possible answers are 2, 3, 5, 7
    fout.write("2\n")
    fout.write("3\n")
    fout.write("5\n")
    fout.write("7\n")

else:       #if N != 1, use recursion to find all answers
    recur([2, 3, 5, 7], 2)      #the first digit that is prime, the length of the number in the current stage of recursion

for i in ans:           #output answers
    fout.write(str(i) + "\n")
