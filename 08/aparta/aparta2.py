def aparta(lista, k):
    i = -1
    while True:
        if not lista[i] % k == 0 and lista[i - 1] % k == 0:
            trocado = lista[i]
            lista[i] = lista[i - 1]
            lista[i - 1] = trocado
    return(lista)
