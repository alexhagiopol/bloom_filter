import BloomFilter as bf

#N = universe size, m = database size, n = hash table size, k = number of hash functions
N = 100
n = 20
m = 10
k = 3
b = bf.BloomFilter(N,n,m,k)
b.add(10)
print b.table_
print b.test(10)