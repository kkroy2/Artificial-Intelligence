import copy
from CSP import CSP
from Queue import Queue
from ComparisonMetrics import ComparisonMetrics as cm


class AC3:
    csp = CSP(0, 0)

    def __init__(self, csp):
        self.csp = csp
        self.csp.mm = cm()

    def run(self):
        self.csp.mm.pStart()
        Q = Queue()
        for e in self.csp.eList:
            Q.put(e)
            tmpE = copy.deepcopy(e)
            tmpE[0] = tmpE[0]+len(self.csp.eList)
            tmp = tmpE[1]
            tmpE[1] = tmpE[2]
            tmpE[2] = tmp
            Q.put(tmpE)

        while not Q.empty():
            e = Q.get()
            revised = self.csp.revise(e[1], e[2])

            if len(self.csp.dm_set[str(e[1])]) == 0:
                return False

            if revised:
                items = self.csp.adj[str(e[1])].items()
                for itm in items:
                    if [itm[1], int(itm[0]), e[1]] not in Q.queue and e[2] != int(itm[0]):
                        Q.put([itm[1], int(itm[0]), e[1]])

        self.csp.mm.pEnd()
        return True
