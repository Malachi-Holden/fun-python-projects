import sys
import time

class Fibb:
    def __init__(self):
        self.solved = [1,1] # self.solved[i] is the ith fibbanocci number

    def fibb(self, n):
        if len(self.solved) > n:
            return self.solved[n]
        #___________
        a = self.fibb(n-1)
        b = self.fibb(n-2)
        self.solved.append(a+b)
        return a + b

def fibbanocci(n):
    F = Fibb()
    return F.fibb(n)

def slowfibb(n):
    if n<=1:
        return 1
    #___
    return slowfibb(n-1) + slowfibb(n-2)


if __name__ == '__main__':
    for n in range(40):
        print("for", n)
        start = time.perf_counter()
        print(slowfibb(n))
        stop = time.perf_counter()
        print("slowfibb:", stop-start, "\n_____\n")
        start = time.perf_counter()
        print(fibbanocci(n))
        stop = time.perf_counter()
        print("fibbanocci:", stop-start, "\n_____\n______\n")
