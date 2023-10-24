var = [1, 2, 3]
var1 = [2, 3]

def iguais():
    return var[0] == var1[0] or var[-1] == var1[-1]

print(iguais())