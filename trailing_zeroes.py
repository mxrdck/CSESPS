from math import floor, log
fac = int(input())

zeros = 0 

while fac >= 5: 
    fac = fac // 5
    zeros += fac

print(zeros)