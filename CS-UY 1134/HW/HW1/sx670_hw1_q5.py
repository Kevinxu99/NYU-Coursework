def fibs(n):
    n0=0
    n1=1
    for i in range(n):
        yield n1
        temp=n0
        n0=n1
        n1=n1+temp
