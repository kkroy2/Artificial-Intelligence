from Constraints import Constraints as cc
from Domains import Domains as dc
from ComparisonMetrics import ComparisonMetrics as cm
import random
import copy


class CSP:

    cons = cc()
    domains = dc(0)
    mm = cm()
    N = 0
    eList = []
    cons_set = {}
    dm_set = {}
    adj = {}
    dmSize = 0
    mat = [[0 for i in range(0, N+1)] for j in range(0, N+1)]

    def __init__(self, N , dmSize):
        self.N = N
        self.eList = []
        self.cons_set = {}
        self.domains = dc(dmSize)
        self.dmSize = dmSize
        for i in range(1 , N+1):
            self.adj[str(i)] = {}
        self.mat = [[0 for i in range(0, N + 1)] for j in range(0, N + 1)]

    def copyByValue(self, cons_set, dm_set, adj, eList, N, dmSize, mat):
        self.cons_set = copy.deepcopy(cons_set)
        self.dm_set = copy.deepcopy(dm_set)
        self.adj = copy.deepcopy(adj)
        self.eList = copy.deepcopy(eList)
        self.N = copy.deepcopy(N)
        self.domains = dc(dmSize)
        self.dmSize = copy.deepcopy(dmSize)
        self.mm = cm()
        self.mat = copy.deepcopy(mat)

    def generatingGraph(self, N):
        mxL = N*(N+1)
        mxL /=2
        edge = random.randint(0, mxL)
        for i in range(0 , edge):
            x = random.randint(1, N)
            y = random.randint(1, N)
            while x == y :
                y = random.randint(1, N)
            self.eList.append([i, x, y])

        # sample case
        #
        # self.eList.append([0, 1, 2])
        # self.eList.append([1, 1, 3])
        # self.eList.append([2, 3, 2])



    def SWAP(self, got):
        tmp = got[1]
        got[1] = got[2]
        got[2] = tmp
        return got

    def setConstraints(self):
        for e in self.eList:
            got = self.cons.assigningConstraints(e[1], e[2])
            self.cons_set[str(e[0])] = got
            self.cons_set[str(e[0]+len(self.eList))] = got

        # sample test case

        # self.cons_set[str(0)]= [8, 1, 2]
        # self.cons_set[str(3)] =[8, 1, 2]
        # self.cons_set[str(1)] = [8, 1, 3]
        # self.cons_set[str(4)] = [8, 1, 3]
        # self.cons_set[str(2)] = [8, 3, 2]
        # self.cons_set[str(5)] = [8, 3, 2]

    def setDomains(self):
        for i in range(1 , self.N+1):
            self.dm_set[str(i)] = self.domains.getDomains()

        # sample test case
        #
        # self.dm_set[str(1)] = [2, 5, 7, 6, 3, -3, -13, 2, 22]
        # self.dm_set[str(2)] = [2, 5, 7, 11, 6, -3, -7, 2, 22]
        # self.dm_set[str(3)] = [2, 4, 8, 9, 14, -3, -11, 2, 22]

    def setAdjcentList(self):
        for e in self.eList:
            self.mat[e[1]][e[2]] = 1
            self.mat[e[2]][e[1]] = 1
            self.adj[str(e[1])][str(e[2])] = e[0]               #adjcent node , edge number
            self.adj[str(e[2])][str(e[1])] = e[0] + len(self.eList)       #reverse edge

    def setMM(self):
        self.mm = cm()

    def revise(self, vi, vj):
        reversed = False
        cur_con = self.adj[str(vi)]             # getting adjacent dictionary
        # print(cur_con)
        cur_con = cur_con[str(vj)]              # getting current edge number
        if cur_con >= len(self.eList):
            reversed = True
        cur_con = self.cons_set[str(cur_con)]   # getting constraints
        changed = False
        tmpRMVL = []
        for xi in self.dm_set[str(vi)]:
            yes = False

            for xj in self.dm_set[str(vj)]:
                tmp_con = copy.deepcopy(cur_con)
                if reversed:
                    tmp_con[1] = xj
                    tmp_con[2] = xi
                else:
                    tmp_con[1] = xi
                    tmp_con[2] = xj

                yes |=self.cons.evaluatingConstraints(tmp_con)

            if yes == False:
                tmpRMVL.append(xi)
                changed |= True
        for tmprmv in tmpRMVL:
            self.dm_set[str(vi)].remove(tmprmv)
        return changed

    def setting(self):
        self.generatingGraph(self.N)
        self.setConstraints()
        self.setDomains()
        self.setAdjcentList()
        self.setMM()












