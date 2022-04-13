import math

ntriangulos = int(input())
triangulos = []
contagem = 0
areasoma = 0

for i in range(ntriangulos):
    z = []
    lados = input()
    for i in range(len(lados)):
        if lados[i] == ' ':
            z.append(i)
    re1 = z[0]
    re2 = z[0] + 1
    re3 = z[1]
    re4 = z[1] + 1

    a = float(lados[0:re1])
    b = float(lados[re2:re3])
    c = float(lados[re4:len(lados)])
    s = (a + b + c)/2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    if area > 100:
        contagem += 1
        areasoma += area
    triangulos.append(f'{area:.2f}')

media = areasoma/contagem


for i in range(ntriangulos):
    print(f'Área {i+1}: {triangulos[i]}')
print(f'Número maiores: {contagem}, área média: {media:.2f}')
