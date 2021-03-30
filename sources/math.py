#def add(a, b):
#    return a + b

def fibo(X):
#    return 1 if X==0 or X==1 else fibo(X-1) + fibo(X-2)
    y1,y2,y = (1,1,1)
    for i in range(1, X):
        y=y1+y2
        y2=y1
        y1=y
    return y
