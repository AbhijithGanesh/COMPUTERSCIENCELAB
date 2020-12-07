#fibonacci


def fibo(x):
    q = 0
    p = 1
    for i in range (x):
        p = p+q
        p,q = q,p
    print(p)
fibo(5)