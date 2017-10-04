# UNSOLVEDs

def valor(a,me,d,h,mi):
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

    return v

def periodo(a1, me1, d1, h1, mi1, a2, me2, d2, h2, mi2):
    minutos = 0
    anos1 = 0
    meses1 = 0
    dias1 = 0
    horas1 = 0
    anos2 = 0
    meses2 = 0
    dias2 = 0
    horas2 = 0

    if a1 > 0:
        anos1 = a1*15
    if me1 > 0:
        meses1 = me1*25
    if d1 > 0:
        dias1 = d1*20
    if h1 > 0:
        horas1 = h1*50
    minutos1 = mi1

    minutos = minutos2 - minutos1
    horas = minutos/50
    dias = horas/20
    meses = dias/25
    anos = meses/15

    print(minutos1, horas1, dias1, meses1, anos1)

periodo(1,0,0,0,0, 2,0,0,0,0)
