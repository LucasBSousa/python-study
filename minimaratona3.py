def estacionamento(a,me,d,h,mi):
    v = 0

    if a > 0:
        v += a*1500
    if me > 0:
        v += me*500
    if d > 0:
        v += d*50
    if h > 0:
        v += h*10
    if mi > 0:
        v += mi*5

    print(v)

estacionamento(1,1,1,1,1)
