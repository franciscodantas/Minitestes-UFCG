def remove(ultimo, menu):
    for x in range(len(ultimo) - 1, -1, -1):
        menu.pop()

def insere_produto(menu, produto, preco):
    troca = False
    for i in range(len(menu)):
        if preco < menu[i][1]:
            ultimo = menu[i: len(menu)]
            remove(ultimo, menu)
            menu.append((produto,preco))
            menu += ultimo
            troca = True
            break
    if troca == False:
        menu.append((produto,preco))
        return menu
    else:
        return menu

