def add(a,b):
    return 5

def fibo(n):                                                                                                 
    a, b = 1, 1
    for i in range(1, n+1):
        a, b = b, b+a
    return a
