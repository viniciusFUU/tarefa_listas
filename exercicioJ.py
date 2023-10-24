def despertador(dia, folga):
    if folga:
        if dia == 0 or dia == 6:
            return 'off'
        else:
            return '10:00'
    else:
        if dia >= 1 and dia <= 5:
            return '07:00'
        else:  
            return '10:00'

print(despertador(1, False))  
print(despertador(0, True))   
print(despertador(5, True))   
