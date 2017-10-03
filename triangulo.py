from maior import maior

def triangulo(x,y,z):
    x = int(x)
    y = int(y)
    z = int(z)

    if maior(x, maior(y,z)) > x+y+z - maior(x, maior(y,z)):
        print('É triângulo')
    else:
        print('Não é triângulo')


a = input('Lado a: ')
b = input('Lado b: ')
c = input('Lado c: ')

triangulo(a,b,c)