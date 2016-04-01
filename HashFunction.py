import random as rand

class HashFunction:
    def __init__(self,i,n,seed):
        self.queries = []
        self.i_ = i #This is the ith hash function we're using
        self.n_ = n #our table has n spaces
        self.seed_ = seed #random seed
    def getHashValue(self,input):
        rand.seed(self.i_*self.seed_)
        return rand.randint(0,self.n_ - 1)
