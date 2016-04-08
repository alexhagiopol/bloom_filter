import HashFunction as hf
import random
import array

class BloomFilter:
    def __init__(self,N,n,m,k): #N = universe size, m = database size, n = hash table size, k = number of hash functions
        self.N_ = N
        self.n_ = n
        self.m_ = m
        self.k_ = k
        self.seed_ = random.randint(0,self.N_)
        self.table_ = [0]*n #initialize table
    def add(self,data):
        indices = []
        for i in range(0,self.k_):
            h = hf.HashFunction(self.n_,self.seed_)
            indices.append(h.getHashValue(data))
        for i in range(0, len(indices)):
            self.table_[indices[i]] = 1
    def test(self,data):
        isPresent = True
        indices = []
        for i in range(0,self.k_):
            h = hf.HashFunction(self.n_,self.seed_)
            indices.append(h.getHashValue(data))
        for i in range(0, len(indices)):
            if self.table_[indices[i]] != 1:
                isPresent = False
        return isPresent