def insere_produto(menu, produto, preco):
    troca = False
    for i in range(len(menu)):
        if preco < menu[i][1]:
            depois = menu[i:len(menu)]
            menu = menu[0:i]
            menu = menu + [(produto,preco)]
            menu = menu + depois
            troca = True
            break
    if troca == False:
        menu.append((produto,preco))
        return menu
    else:
        return menu

menu = [("expresso", 5.29), ("duplo", 8.09), ("capuccino", 10.59)]
print(insere_produto(menu, "latte", 6.59))


