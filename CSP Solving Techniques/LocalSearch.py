import random
import time


def initial_asst(n):
    ast =[[0 for i in range(n)]for j in range(n)]
    for x in range(n):
        id = random.randint(0 , n-1)
        ast[x][id] = 1
    return ast


def isOkay(ast , x ,y , n):
    cnt = 0
    for i in range(x+1 , n):
        # print(i , y)
        cnt +=ast[i][y]

    for i in range(0 , x):
        # print(i , y)
        cnt +=ast[i][y]

    for j in range(y + 1, n):
        # print(x, j)
        cnt += ast[x][j]

    for j in range(0, y):
        # print(x, j)
        cnt += ast[x][j]

    for i in range(1 , min(n-x , n-y)):
        # print(x+i , y+i)
        cnt += ast[x+i][y+i]

    for i in range(1, min(x, n - y-1)+1):
        # print(x - i, y + i)
        cnt += ast[x - i][y + i]

    for i in range(1, min(n-x-1, y)+1):
        # print(x + i, y - i)
        cnt += ast[x + i][y - i]

    for i in range(1, min(x, y)+1):
        # print(x - i, y - i)
        cnt += ast[x - i][y - i]

    return cnt


def isSolution(ast , n):
    ret = 0
    for i in range(0 , n):
        for j in range(0 ,n):
            if ast[i][j]==1:
                ret += isOkay(ast , i , j , n)
    return ret

total_iteration = 0


def MIN_Conflicts( max_steps ,ast,  n):
    global total_iteration
    total_iteration = 0

    for i in range(0 , max_steps):
        total_iteration +=1
        if isSolution(ast , n)==0: 
            return ast
        idx = -1
        idy = -1

        mx = 1000000000000
        # for i in range(0, n):
        now = random.randint(0 , n-1)
        i = now
        # print(now , ": now")
        print('Selected Variable : ', now)
        for j in range(0, n):
            # print(i , j , ast[i][j])
            if ast[i][j] == 1:
                pidx = i
                pidy = j
                idx = i
                idy = j
                ret = isOkay(ast , i , j , n)
                for j in range(0, n):
                    if j!=pidy:
                        ret = isOkay(ast, idx, j, n)-1
                    if ret < mx:
                        mx = ret
                        idy = j
                # print('MnF: ', idx , idy, mx)
                ast[pidx][pidy] = 0
                ast[idx][idy] = 1
        print('After resolving: ',)
        Output(ast , n)
    return []


def Output(ast , n):
    for i in range(0 , n):
            print(ast[i])


if __name__=='__main__':
    start = time.time()
    n = 8
    ast = initial_asst(n)
    # ast = [[0, 0, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    print("INITIAL: ", ast)
    ast = MIN_Conflicts(1000000, ast , n )
    if len(ast)==0:
        print("FAILED")
    else:
        Output(ast , n)
    end = time.time()
    print('Need Time(ms): ', end-start)
    print('Total Iteration: ', total_iteration)
    # ar = [8 , 10 , 15, 20]
    # for i in ar:
    #     start = time.time()
    #     n = i
    #     print('For ', i)
    #     ast = initial_asst(n)
    #     # ast = [[0, 0, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0]]
    #     print("INITIAL: ")
    #     Output(ast , n)
    #     ast = MIN_Conflicts(1000000, ast, n)
    #     if len(ast) == 0:
    #         print("FAILED")
    #     else:
    #         print('FinaL: ')
    #         Output(ast, n)
    #     end = time.time()
    #     print('Need Time(ms): ', end - start)
    #     print('Total Iteration: ', total_iteration)
    #     print('')
    #     print('')





