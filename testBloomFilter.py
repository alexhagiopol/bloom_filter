import BloomFilter as bf
import math
import random

N = 100
m = 20
iter = 10000

for n in [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]:
    c = float(n) / float(m)
    k = int(round(c*math.log(2)))
    print "TESTING: c = ", c, " n = ", n, " m = ", m, " k = ", k, "real k = " , c*math.log(2), " ratio = ", c*math.log(2)/k
    falsePositives = 0
    for j in range(0,iter):
        #print "n = ",n," iter = ", j
        b = bf.BloomFilter(N, n, m, k)
        randTarget = random.randint(0,m)
        for k in range(0,m+1): #add every number including m
            if k != randTarget:
                b.add(k)
        if b.test(randTarget):
            falsePositives  = falsePositives + 1
    print "NUMBER OF FALSE POSITIVES =", falsePositives

