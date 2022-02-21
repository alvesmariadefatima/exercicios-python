dinheiro = float(input('Qual é o preço do produto? R$'))
porcentagem = dinheiro - (dinheiro * 5 / 100)

print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar {:.2f}'.format(dinheiro, porcentagem))

