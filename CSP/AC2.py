from CSP import CSP
from Queue import Queue
from ComparisonMetrics import ComparisonMetrics as cm
import copy


class AC2:

    csp = CSP(0, 0)

    def __init__(self, csp):
        self.csp = csp
        self.csp.mm = cm()

    def run(self):
        self.csp.mm.pStart()
        for i in range(1, self.csp.N+1):
            frwdq = Queue()
            backq = Queue()

            for j in range(1, self.csp.N+1):
                if j < i:
                    if self.csp.mat[i][j] == 1:
                        frwdq.put([i, j])
                        backq.put([j, i])

            while not frwdq.empty():
                while not frwdq.empty():
                    cur_edge = frwdq.get()
                    revised = self.csp.revise(cur_edge[0], cur_edge[1])

                    if len(self.csp.dm_set[str(cur_edge[0])]) == 0:
                        return False
                    if revised:
                        for j in range(1, i+1):
                            if j <= i and j != cur_edge[1]:
                                if self.csp.mat[cur_edge[0]][j] == 1 and self.csp.mat[j][cur_edge[0]] == 1:
                                    if [j, cur_edge[0]] not in backq.queue:
                                        backq.put([j, cur_edge[0]])
                frwdq = backq
                backq = Queue()
        self.csp.mm.pEnd()
        return True


