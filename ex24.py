from math import sqrt
from time import time

nmax = 100

for a in range(1,nmax+1) :
    for b in range(a+1,nmax+1) :
        c = sqrt(a**2 + b**2)
        if c % 1 == 0: # int(c) == c
            print("%5d %5d %5d" %(a,b,c))
