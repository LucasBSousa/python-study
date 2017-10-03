from maior import maior

for x in range(1,11):
    for y in range(1,11):
        for z in range(1,11):
            m = maior(x, maior(y,z))
            if m**2 == x**2 + y**2 + z**2 - m**2:
                print(x,y,z)
