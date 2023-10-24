var = [1, 2]


def soma(num):
    if len(num) >= 1:
        return num[0] + num[1]
    elif len(num) == 1:
        return num[1]
    else:
        return 0


print(soma(var))
