def remove_ocorrencias(lista, elemento):
    removeu = None
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == elemento:
            lista.pop(i)
            removeu = elemento

    return removeu
