import time


class ComparisonMetrics():

    # this section for calculating the running time
    start = 0
    end = 0
    total_running_time=0

    def pStart(self):
        self.start = time.time()

    def pEnd(self):
        self.end = time.time()

    def pRun(self):
        print(self.end, self.start)
        return self.end-self.start

