def rotesq(valores):
    valores[0],valores[len(valores)-1] = valores[len(valores)-1],valores[0]
    return valores

print(rotesq([0,10,20]))
