def fatorial(x):
    f = 1
    for d in range(1,x+1):
        print(f,d)
        f *= d
    return f

print(fatorial(4))