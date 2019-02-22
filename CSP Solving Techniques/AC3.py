from Queue import Queue

D = {}
con = {}


def isSatisfied(vi, vj, cd):
    if cd[0][0] == str(vi):
        if vj % vi == 0:
            return True
        else:
            return False
    else:
        if vi % vj == 0:
            return True
        else:
            return False


def Revise(vi, vj):
    print(vi , vj, ' revised...')
    revised = False
    for xi in D.get(str(vi)):
        # print(xi , type(xi))
        exist = False
        for xj in D.get(str(vj)):
            exist |= isSatisfied(xi, xj, con.get(str(vi)))
            if exist == False:
                print("herer : ", D.get(str(vi)), vi)
                D.get(str(vi)).remove(xi)
                print("After: ", D.get(str(vi)))
                revised = True
    return revised


edge = []
adj = {}

def AC3():
    q = Queue()
    for e in edge:
        q.put(e)
        print(e)
        q.put([ e[0] , e[1] ])
    while(q.empty()==False):
        e = q.get()
        print(q.qsize(), ' size ---------')
        print("get Edge: ", e)
        revised = Revise(int(e[0]), int(e[1]))
        print(D.get(str(e[0])), " herer")
        if len(D.get(str(e[0]))) == 0:
            return False
        if revised== True:
            adjList = adj.get(str(e[0]))
            for i in adjList:
                q.put([i,e[0]])
    return True


if __name__=='__main__':
    edge.append([2 , 3])
    edge.append([1, 3])
    adj['1']=  [3]
    adj['2']=[3]
    adj['3']= [1 , 2]

    D['1'] = [2, 5]
    D['2'] = [2, 4]
    D['3'] = [2, 5]
    con['1'] =  ['3|1']
    con ['2'] = ['3|2']
    con['3'] = ['3|1' , '3|2']
    AC3()
    for i in range(1 , 4):
        print(i ,": ", D.get(str(i)))
        print('fucked')


