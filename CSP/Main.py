from CSP import CSP as csp
from AC1 import AC1
from AC3 import AC3
from AC2 import AC2
from AC4 import AC4

import copy
import random
if __name__ =='__main__':
    # N= input('Number of Nodes: ',)
    # dmSize = input('Size of Domains: ',)
    cnt = 0
    total = 0
    # for i in range(0 ,100):
    while total != 20:
        # N = random.randint(1, 5)
        # dmSize = random.randint(10, 20)
        # print(N, dmSize, "N && dmSize")
        N = 5
        dmSize = 10
        csp0 = csp(N, dmSize)
        csp0.setting()
        # print(csp0.adj)
        csp1 = csp(0 , 0)
        csp1.copyByValue(csp0.cons_set, csp0.dm_set, csp0.adj,
                         csp0.eList,csp0.N, csp0.dmSize, csp0.mat)
        csp2 = csp(0 , 0)
        csp2.copyByValue(csp0.cons_set, csp0.dm_set, csp0.adj,
                         csp0.eList, csp0.N, csp0.dmSize , csp0.mat)

        csp3 = csp(0, 0)
        csp3.copyByValue(csp0.cons_set, csp0.dm_set, csp0.adj,
                         csp0.eList, csp0.N, csp0.dmSize, csp0.mat)

        csp4 = csp(0, 0)
        csp4.copyByValue(csp0.cons_set, csp0.dm_set, csp0.adj,
                         csp0.eList, csp0.N, csp0.dmSize, csp0.mat)
        # print(csp1.dm_set)
        print(csp1.cons_set)
        # print(csp1.adj)
        # for i in range(1, N+1):
        #     print('Domains for ', i, ' ', csp1.dm_set[str(i)])
        # for i in range(1, N+1):
        #     print('Domains for ', i, ' ', csp3.dm_set[str(i)])
        # for i in csp1.cons_set:
        #     print(' Cons: ',i)
        # for i in csp3.cons_set:
        #     print('Cons: ',i)
        # print(csp1.eList)
        # print(csp3.eList)

        print('AC1 output: ')
        ac1 = AC1(csp1)
        consistent1 = ac1.run()
        # for i in range(1, N+1):
        #     print('111 Domains for ',i,' ',ac1.csp.dm_set[str(i)])
        #
        # print(ac1.csp.mm.pRun())
        if consistent1:
            print(ac1.csp.mm.pRun())
        else:
            print('No, It is not consistent!')
        # ac1 = AC1(csp2)
        # ac1.run()
        # print(ac1.csp.mm.pRun())
        # print()
        ac2 = AC2(csp2)
        consistent2 = ac2.run()

        print('AC2 output: ')
        # for i in range(1, N+1):
        #     print('222 Domains for ', i, ' ', ac2.csp.dm_set[str(i)])
        #
        if consistent2:
            print(ac2.csp.mm.pRun())
        else:
            print('No, It is not consistent!')

        print('AC3 output: ')
        ac3 = AC3(csp3)
        consistent3 = ac3.run()
        # for i in range(1, N+1):
        #     print('333 Domains for ',i,' ',ac3.csp.dm_set[str(i)])
        if consistent3 == True:
            print(ac3.csp.mm.pRun())
        else:
            print('No, It is not consistent!')

        print('AC4 output: ')
        ac4 = AC4(csp4)
        consistent4 = ac4.run()
        # for i in range(1, N+1):
        #     print('444 Domains for ',i,' ',ac4.csp.dm_set[str(i)])
        if consistent4 == True:
            print(ac4.csp.mm.pRun())
            # for i in range(1, N+1):
            #     print('444 Domains for ',i,' ',ac4.csp.dm_set[str(i)])
        else:
            print('No, It is not consistent!')
        if consistent1 and consistent3 and consistent4 and consistent2:
            total +=1
            tmp_cnt = 0
            for i in range(1, N+1):
                if ac1.csp.dm_set[str(i)]== ac3.csp.dm_set[str(i)] and ac2.csp.dm_set[str(i)] == ac1.csp.dm_set[str(i)]\
                         and ac4.csp.dm_set[str(i)] == ac1.csp.dm_set[str(i)]:
                    tmp_cnt +=1
                else:
                    print(ac1.csp.dm_set[str(i)], i)
                    print(ac4.csp.dm_set[str(i)] , i)
            if tmp_cnt == 5:
                cnt +=1
        if consistent2 and consistent1 and consistent3 and not consistent4:
            for i in range(1, N+1):
                if not (ac1.csp.dm_set[str(i)]== ac3.csp.dm_set[str(i)] and ac2.csp.dm_set[str(i)] == ac1.csp.dm_set[str(i)]\
                         and ac4.csp.dm_set[str(i)] == ac1.csp.dm_set[str(i)]):
                    print(ac1.csp.dm_set[str(i)] , i )
                    print(ac4.csp.dm_set[str(i)] , i)
        print()
        print()
        print()
    print(total, ' ', cnt)








