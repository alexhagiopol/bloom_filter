import random as rand

class HashFunction:
    def __init__(self,n,seed):
        self.queries = []
        self.n_ = n #our table has n spaces
        self.seed_ = seed #random seed
    def getHashValue(self,input):
        rand.seed(self.seed_*input)
        hashValue = rand.randint(0,self.n_ - 1)
        #print "SEED = ",self.i_*self.seed_, " INPUT = ", input, " HASH VALUE = ", hashValue
        return hashValue
