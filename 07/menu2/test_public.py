from undertst import insere_produto

def test_exemplo_1():
    menu = [("expresso", 5.29), ("duplo", 8.09), ("capuccino", 10.59)]
    insere_produto(menu, "latte", 9.59)
    assert menu == [("expresso", 5.29), ("duplo", 8.09), 
                    ("latte", 9.59), ("capuccino", 10.59)]

def test_exemplo_2():
    menu = [("agua", 3.15), ("refrigerante", 4.10), ("suco_laranja", 7.39)]
    insere_produto(menu, "agua_gas", 4.80)
    assert menu == [("agua", 3.15), ("refrigerante", 4.10),
                    ("agua_gas", 4.80), ("suco_laranja", 7.39)]
