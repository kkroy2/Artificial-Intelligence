import random


class Domains():

    D = []
    sz = 0

    def __init__(self, sz):
        self.sz = sz

    def choosingDomains(self, x):
        if x==0:
            return self.numericDomains()
        else:
            return self.nonNumericDomains()

    def numericDomains(self):
        tmp = random.randint(-103, 103)
        while tmp == 0:
            tmp = random.randint(-103, 103)
        return tmp

    def nonNumericDomains(self):
        iter = random.randint(1, 5)
        s = ''
        for i in range(0 , iter):
            tmp = random.randint(0, 126)
            tmp = chr(tmp)
            s += tmp
        return self.hash(s)

    def hash(self, s):
        p = 1
        val = 0
        for ch in s:
            val += ord(ch) * p
            val = val%103
            p =(p*13) % 103
        if val == 0:
            val = 103
        return val

    def getDomains(self):
        self.D =[]
        for i in range(0, self.sz):
            typ = random.randint(0, 1)
            self.D.append(self.choosingDomains(typ))
        return self.D



