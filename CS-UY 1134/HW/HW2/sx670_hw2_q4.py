def e_approx(n):
    e=1
    fac=1
    for i in range(1,n+1):
        fac=fac*i
        e+=(1/fac)
    return e

