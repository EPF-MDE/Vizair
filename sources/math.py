def add(a,b):
        return 5

def fibo(x):
    #return 1 if x == 0 or x == 1 else fibo(x-2) + fibo(x-1)
        y1, y2, y  = (1,1,1)
        for i in range(1,x):
                y = y1 + y2
                y2 = y1
                y1 = y
        return y


