quant = []

while True:
    nomes = input()
    if nomes == "-":
        break
    quant.append(nomes)
if len(quant) == 11:
    print("Modalidade -> Futebol")
elif len(quant) == 5:
    print("Modalidade -> Basquete")
elif len(quant) == 6:
    print("Modalidade -> Vôlei")
elif len(quant) == 7:
    print("Modalidade -> Handebol")
else:
    print("Equipe Inválida")
    
