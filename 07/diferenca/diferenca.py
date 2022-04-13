def diferenca_listas(lista1,lista2):
    diferenca =  []
    if lista1 > lista2:
        limite =  len(lista1)
    else:
        limite = len(lista2)

    for i in range(limite-1,-1,-1):
        for x in range(limite-1,-1,-1):
            if lista1[i] == lista2[x]:
                lista1.pop(i)
                diferenca.append(lista2[x])
    return lista1

lista1 = [1, 3, 4]
lista2 = [4,1,3,5,6]
print(diferenca_listas(lista1, lista2))
print(lista1)
