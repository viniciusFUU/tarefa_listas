var = [1, 2, 3, 5, 9]
var1 = [1, 4, 2]


def meio(num, num2):
    #dividindo por inteiro para que possa pegar o proximo num, onde devolve o inteiro
    meia_a = len(num)//2
    meia_b = len(num2)//2
    return num[meia_a], num2[meia_b]


print(meio(var, var1))
