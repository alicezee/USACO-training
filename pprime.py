""""
LANG: PYTHON3
TASK: pprime
"""
import math

fin = open("pprime.in", "r")        #open input/output files
fout = open("pprime.out", "w")

ranges = list(map(int, fin.readline().strip().split()))     #read in a and b
palindromes = []        #store palindromes

if ranges[0] % 2 == 0:      #check if "a" is even (even numbers cannot be prime)
    ranges[0] += 1

sDigits = math.ceil(len(str(ranges[0]))/2)
eDigits = math.ceil(len(str(ranges[1]))/2)
start = pow(10, sDigits-1)      #starting range of palindromes
end = int(str(ranges[1])[:eDigits]) * 10        #ending range of palindromes

for i in range(start, end+1):       #construct palindromes

    if int(str(i)[0]) % 2 == 0:     #check for even numbers
        continue

    if len(str(i)) > 1:
        if (int(str(i) + str(math.floor(i/10))[::-1])) > ranges[1]:     #check if palindrome is out of range (palindromes > b)
            break
        palindromes.append(int(str(i) + str(math.floor(i/10))[::-1]))       #odd digit palindromes ex: 12 --> 121

    elif len(str(i)) == 1:
        palindromes.append(i)       #single digit palindromes ex: 2, 3, 5, 7

    palindromes.append(int(str(i) + str(i)[::-1]))      #even digit palindromes ex: 12 --> 1221

palindromes.sort()      #sort palindromes from least to greatest


j = 0
isPrime = True
while j < len(palindromes):     #iterate palindromes
    if palindromes[j] % 2 == 0 or palindromes[j] > ranges[1] or palindromes[j] < ranges[0]:     #check for even palindromes and out of range palindromes(palindrome < a or palindrome > b)
        palindromes.pop(j)
        continue

    isPrime = True
    for k in range(3, int(math.sqrt(palindromes[j]))+ 1, 2):        #check for prime
        if palindromes[j]%k == 0:
            palindromes.pop(j)
            isPrime = False
            break
    if isPrime:
        j += 1

for l in palindromes:       #output
    fout.write(str(l) + "\n")

