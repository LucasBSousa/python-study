def triangulo(x,y,z):
    x = int(x)
    y = int(y)
    z = int(z)

    if x == y and x == z and y == z: 
        print('Triângulo equilátero')
    else:
        if x != y and x != z and y != z:
            print('Triângulo escaleno')
        else:
            print('Triângulo isóceles')


a = input('Lado a: ')
b = input('Lado b: ')
c = input('Lado c: ')

triangulo(a,b,c)