

class Constraints:
    cons_st = []

    def __init__(self):

        self.cons_st=['==', '!=', '<', 'square',
                      'cube', 'sqrt', 'gcd',
                      'congruent', 'divisible',
                      'hash==','hash!=']

    def assigningConstraints(self, x, y):
        ret = x*10 + y
        ret %=11
        tmpCons = [ret, x , y]
        return tmpCons

    def GCD(self, a , b):
        if b==0:
            return a
        return self.GCD(b , a%b)

    def C_HASH(self, x):
        return x

    def evaluatingConstraints(self, con):

        if self.cons_st[con[0]]=='==':
            return con[1] == con[2]

        elif self.cons_st[con[0]]=='!=':
            return con[1]!=con[2]

        elif self.cons_st[con[0]] == '<':
            return con[1] < con[2]

        elif self.cons_st[con[0]] == 'square':
            return con[1] == con[2]**2

        elif self.cons_st[con[0]] == 'cube':
            return con[1] == con[2]**3

        elif self.cons_st[con[0]] == 'sqrt':
            return con[1]*con[1] == con[2]

        elif self.cons_st[con[0]] == 'gcd':
            return self.GCD(con[1], con[2]) == 1

        elif self.cons_st[con[0]] =='congruent':
            return (con[1]*con[2]) % 103 == 1

        elif self.cons_st[con[0]] =='divisible':
            return con[2] % con[1] == 0

        elif self.cons_st[con[0]] =='hash==':
            return self.C_HASH(con[1]) == self.C_HASH(con[2])

        elif self.cons_st[con[0]] =='hash!=':
            return self.C_HASH(con[1]) != self.C_HASH(con[2])
        else:
            return False
