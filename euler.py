from fatorial import fatorial

def euler1(n):
    e = 0
    for x in range(0,n):
        e = e + 1/fatorial(2*x+1)
    return e

def euler2(n):
    i = 0
    e = 0
    p = 1/fatorial(2*i+1)
    while p >= n:
        e = e + p
        i += 1
        p = 1/fatorial(2*i+1)
    return e

def euler3(n):
    i = 0
    e = 0
    p = 1/fatorial(2*i+1)
    d = 0
    while abs(p-d) > n:
        e = e + p
        d = p
        i += 1
        p = 1/fatorial(2*i+1)
    return e

print(iteracoes3(0.00000000000000000001))