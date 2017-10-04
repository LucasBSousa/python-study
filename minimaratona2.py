from primo import primo

def fatoracao(n):
    x = n
    for d in range(n,1,-1):
        if primo(d) == True:
            if n % d == 0:
                print(n,d)
                n = n // d
    if n != 1 and n > d:
        for d in range(n,1,-1):
            if primo(d) == True:
                if n % d == 0:
                    print(n,d)
                    n = n // d
    if n != 1 and n > d:
        for d in range(n,1,-1):
            if primo(d) == True:
                if n % d == 0:
                    print(n,d)
                    n = n // d
    if n != 1:
        if n % d == 0:
            print(n,d)
            n = n // d
        if n == x:
            print(n,x)
            n = n // x
    print(n)

fatoracao(35)
