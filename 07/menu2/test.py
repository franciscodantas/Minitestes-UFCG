from menu3 import insere_produto

def test_exemplo_1():
    menu = [("expresso", 5.29), ("duplo", 8.09), ("capuccino", 10.59)]
    insere_produto(menu, "latte", 8.09)
    print(menu)

test_exemplo_1()

