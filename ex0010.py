real = float(input('Quanto dinheiro em R$ você tem na carteira: '))
dolar = real / 5.15

dolar_na_carteira = float(input('Quanto dinheiro em U$ você tem na carteira? '))
dolar_convertido = 5.15 * real 

print('Com R$ {:.2f} você pode comprar U$ {:.2f} '.format(real, dolar))
print('Com U$ {:.2f} você pode comprar R$ {:.2f} '.format(dolar_na_carteira, dolar_convertido))