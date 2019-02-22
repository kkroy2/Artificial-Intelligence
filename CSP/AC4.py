from Queue import Queue
from CSP import CSP
from ComparisonMetrics import ComparisonMetrics as cm
import copy


class AC4:
    csp = CSP(0, 0)
    mList = []
    support = {}                        #   list in dictionary in dictionary
    counter = {}                        #   value in dictionary in dictionary
    tmpList = []
    offset = 1003
    Q = Queue()
    visited = {}

    def __init__(self, csp):
        self.csp = csp
        self.csp.mm = cm()

    def preINIT(self):
        for i in range(1, self.csp.N+1):
            for j in range(0, len(self.csp.dm_set[str(i)])):
                if self.csp.dm_set[str(i)][j] < 0:
                    self.csp.dm_set[str(i)][j] += self.offset

        for i in range(1, self.csp.N+1):
            self.support[str(i)] = {}
            self.counter[str(i)] = {}
            self.visited[str(i)] = {}
            for j in self.csp.dm_set[str(i)]:
                self.support[str(i)][str(j)] = []
                self.visited[str(i)][str(j)] = 0
                self.counter[str(i)][str(j)] = {}
                for k in range(1, self.csp.N+1):
                    self.counter[str(i)][str(j)][str(k)] = 0

    def postBack(self):
        for i in range(1, self.csp.N+1):
            for j in range(0, len(self.csp.dm_set[str(i)])):
                if self.csp.dm_set[str(i)][j] > 103:
                    self.csp.dm_set[str(i)][j] -= self.offset

    def initialize(self):
        self.preINIT()
        for node in range(1, self.csp.N+1):
            tmpAdj = copy.deepcopy(self.csp.adj[str(node)])
            uNode = copy.deepcopy(node)
            tmpAdj = tmpAdj.items()
            for itm in tmpAdj:
                vNode = int(itm[0])
                edgeNum = int(itm[1])
                is_reversed = False
                if edgeNum >= len(self.csp.eList):
                    is_reversed = True

                for uDV in self.csp.dm_set[str(uNode)]:
                    for vDV in self.csp.dm_set[str(vNode)]:
                        curCon = copy.deepcopy(self.csp.cons_set[str(edgeNum)])
                        yes = False
                        if is_reversed:
                            curCon[2] = uDV
                            if curCon[2] > 103:
                                curCon[2] -= self.offset
                            curCon[1] = vDV
                            if curCon[1] > 103:
                                curCon[1] -= self.offset
                        else:
                            curCon[1] = uDV
                            if curCon[1] > 103:
                                curCon[1] -= self.offset
                            curCon[2] = vDV
                            if curCon[2] > 103:
                                curCon[2] -= self.offset
                        yes = self.csp.cons.evaluatingConstraints(curCon)
                        # print('Evaluating ', curCon, ' result: ',yes, ' at:', uNode)
                        if yes:
                            # print('Push: ', [vNode, vDV], ' at ',[uNode, uDV])
                            self.support[str(uNode)][str(uDV)].append([vNode, vDV])
                            self.counter[str(uNode)][str(uDV)][str(vNode)] += 1

        # for node in range(1 , self.csp.N+1):
        #     for val in self.csp.dm_set[str(node)]:
        #         # self.counter[str(node)][str(val)] = len(self.support[str(node)][str(val)])
        #         print([node, val], ': ', self.counter[str(node)][str(val)], ' : ', self.support[str(node)][str(val)])

    def getDomainBack(self):
        for i in range(1 , self.csp.N+1):
            self.csp.dm_set[str(i)] = []
        for itm in self.mList:
            if itm[1] not in self.csp.dm_set[str(itm[0])]:
                self.csp.dm_set[str(itm[0])].append(itm[1])
        return

    def run(self):
        self.csp.mm.pStart()
        self.initialize()
        self.Q = Queue()
        self.mList = []
        for i in range(1, self.csp.N+1):
            tmpRVL = set()
            for j in self.csp.dm_set[str(i)]:
                for k in range(1, self.csp.N+1):
                    if int(i) != int(k) and self.csp.mat[i][k] == 1:
                        if self.counter[str(i)][str(j)][str(k)] == 0:
                            if j in self.csp.dm_set[str(i)]:
                                tmpRVL.add(j)
                                # self.mList.append([[i, j]])
                                if self.visited[str(i)][str(j)] == 0:
                                    # print('Queue pushing: ', [i, j])
                                    self.visited[str(i)][str(j)] = 1
                                    self.Q.put([int(i), int(j)])
            # print(tmpRVL)
            for tmprvl in tmpRVL:
                self.csp.dm_set[str(i)].remove(tmprvl)
            if len(self.csp.dm_set[str(i)]) == 0:
                self.csp.mm.pEnd()
                return False

        while not self.Q.empty():

            tmp = self.Q.get()
            self.mList.append(tmp)
            for xa in self.support[str(tmp[0])][str(tmp[1])]:
                if xa[1] in self.csp.dm_set[str(xa[0])] and self.csp.mat[xa[0]][tmp[0]] == 1 and self.csp.mat[tmp[0]][xa[0]] == 1:
                    self.counter[str(xa[0])][str(xa[1])][str(tmp[0])] -= 1
                    if self.counter[str(xa[0])][str(xa[1])][str(tmp[0])] == 0:
                        if self.visited[str(xa[0])][str(xa[1])] == 0:
                            self.visited[str(xa[0])][str(xa[1])] = 1
                            self.csp.dm_set[str(str(xa[0]))].remove(xa[1])
                            if len(self.csp.dm_set[str(xa[0])]) ==0:
                                self.csp.mm.pEnd()
                                return False
                            self.Q.put([xa[0], xa[1]])

        for tmprvl in self.mList:
            if tmprvl[1] in self.csp.dm_set[str(tmprvl[0])]:
                self.csp.dm_set[str(tmprvl[0])].remove(tmprvl[1])
            if len(self.csp.dm_set[str(tmprvl[0])]) == 0:
                self.csp.mm.pEnd()
                return False

        # self.getDomainBack()
        for i in range(1, self.csp.N+1):
            if len(self.csp.dm_set[str(i)]) == 0:
                return False
        self.postBack()
        self.csp.mm.pEnd()
        return True

