def maior_slice(lista):
    sequencia = []
    todos = []
    saida = []

    for i in range(len(lista)-1):
        for x in range(i,len(lista)-1):
            todos.append(sequencia)
            if lista[i] < lista[i + 1]:
                sequencia.append(lista[i])
            else: break
    for i in range(len(todos)-1):
        if saida < todos[i]:
            saida = todos[i]

    return saida

