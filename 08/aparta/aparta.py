def aparta(lista, k):
    apartado = 0
    for x in range(len(lista)):
        for i in range(len(lista) - 1, 0, -1):
            if not lista[i] % k == 0 and lista[i - 1] % k == 0:
                trocado = lista[i]
                lista[i] = lista[i - 1]
                lista[i - 1] = trocado
        if lista[x] % k == 0:
            apartado += 1

    return apartado
