def primo(x):
    if x == 2:
        return True
    else:
        for d in range(2, x-1):
            if (x % d) == 0:
                return False
        return True

for x in range(1,30):
    if primo(x) == True:
        print(x)