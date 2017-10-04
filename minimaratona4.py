# UNSOLVED

def direcao(x,y):
    hipotenusa = (x**2 + y**2)**0.5
    sen = y/hipotenusa
    cos = y/hipotenusa
    tg = sen/cos

    if x>0 and y>0:
        if cos > -0.5 and cos <= 0.5:
            return "N"
        if cos > 0.5 and cos <= 0.866:
            return "NE"
        if cos > 0.866 and cos <= 1:
            return "E"
    if x<0 and y>0:
        if cos > 0.866 and cos <= 1:
            return "E"
        if cos > -0.5 and cos < 0.5:
            return "SE"
        if cos > -0.5 and cos < 0.5:
            return "S"
        if cos > -0.5 and cos < 0.5:
            return "SW"
    if x>0 and y<0:
        if cos > -0.5 and cos < 0.5:
            return "W"
        if cos > -0.5 and cos < 0.5:
            return "NW"
    if x<0 and y<0:
        if cos > -0.5 and cos < 0.5:
            return "W"
        if cos > -0.5 and cos < 0.5:
            return "NW"

    print(cos)

print(direcao(-1,5))