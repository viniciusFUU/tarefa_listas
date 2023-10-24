def conseguir_mesa(nota_sua, nota_par):
    if nota_sua <= 2 or nota_par <= 2:
        return 0
    elif nota_sua >= 8 or nota_par >= 8:
        return 2
    else:
        return 1


print(conseguir_mesa(7, 9))
print(conseguir_mesa(3, 2))
print(conseguir_mesa(9, 5))
