def temp(t):
    if t >= 60 and t <= 90:
        return print("Esquilos saíram para brincar")
    elif t > 90 and t <= 100:
        return print("É verão e os esquilos saíram para brincar")
    else:
        return print("Os esquilos não saíram para brincar")


temperatura = 91

temp(temperatura)
