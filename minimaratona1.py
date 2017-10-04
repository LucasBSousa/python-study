def combinacoesSem(n):
    for x in range(0,n+1):
        for y in range(0,n+1):
            for z in range(0,n+1):
                if z!=x and x!=y and y!=z:
                    print(x,y,z)

def combinacoesCom(n):
    for x in range(0,n+1):
        for y in range(0,n+1):
            for z in range(0,n+1):
                print(x,y,z)

combinacoesSem(1)
combinacoesCom(1)