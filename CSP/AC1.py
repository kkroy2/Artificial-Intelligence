from CSP import CSP
from ComparisonMetrics import ComparisonMetrics as cm


class AC1:
    csp = CSP(0 , 0)

    def __init__(self , csp):
        self.csp = csp
        self.csp.mm = cm()

    def run(self):
        self.csp.mm.pStart()
        changed = True
        while changed:
            changed = False
            for e in self.csp.eList:
                changed |= self.csp.revise(e[1], e[2])
                changed |= self.csp.revise(e[2], e[1])
        self.csp.mm.pEnd()

        for i in range(1, self.csp.N+1):
            if len(self.csp.dm_set[str(i)])==0:
                return False
        return True






