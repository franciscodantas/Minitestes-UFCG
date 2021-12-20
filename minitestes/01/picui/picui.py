atual = float(input())
tentativa = float(input())

if atual == tentativa:
    print('recorde empatado')
elif atual < tentativa:
    print(f'recorde quebrado ({tentativa} kg)')
else:
    print('recorde mantido')
