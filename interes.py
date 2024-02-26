def valor_futuro(va,i,n):
    return va * (1+i)**n
va=10000
i=3.5
n=7

print(valor_futuro(va, i/100, n))