def multa(v):
    multa = 0
    if v <= 60:
        return print("Sem multa")
    elif v > 60 and v <= 80:
        multa += 1
        return print(f"Você recebeu multa média e ganhou um ponto na carteira")
    else:
        multa += 2
        return print(f"Você recebeu uma multa grave e recebeu 2 pontos na carteira")


velocidade = 99

multa(velocidade)
