def insere_produto(menu, produto, preco):
    for i in range(menu):
        ultimo = False
        if preco < menu[i][1]: break
        else: ultimo = True

    menu.append(None)
    for x in range(len(menu) - 1, i, -1):
        menu[x] = menu[x - 1]

    if ultimo:
        menu[-1] = (produto,preco)
    else:
        menu[x] = (produto,preco)

    return menu

