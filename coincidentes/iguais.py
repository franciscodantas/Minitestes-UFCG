def so_coincidentes(M1, M2):
    matriz_igual = []
    coluna_iguais = []
    for linha in range(len(M1)):
        for coluna in range(len(M1[0])):
                if M1[linha][coluna] == M2[linha][coluna]:
                    coluna_iguais.append(M2[linha][coluna])
                else:
                    coluna_iguais.append(0)
                if len(coluna_iguais) == len(M2[0]):
                    matriz_igual.append(coluna_iguais)
                    coluna_iguais = []
    return matriz_igual

