comprimento = float(input())
largura =  float(input())
profundidade = float(input())

m3 = comprimento * largura * profundidade
litros = m3 * 1000

print(f'A piscina comporta {litros:.2f} litros de água.')
