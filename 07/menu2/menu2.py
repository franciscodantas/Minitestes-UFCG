def insere_produto(menu, produto, preco):
    troca = False
    menu.append((produto,preco))
    for i in range(len(menu) - 1, -1, -1):
        if preco < menu[i][1]:
            trocado = menu[i]
            menu[i] = (produto,preco)
            menu[i + 1] = trocado
    
    return menu

