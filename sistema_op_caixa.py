print('-'*12)
preco_mercadoria1 = float(input('Digite o preço da mercadoria: R$ '))
preco_mercadoria2 = float(input('Digite o preço da mercadoria: R$ '))
preco_mercadoria3 = float(input('Digite o preço da mercadoria: R$ '))
preco_mercadoria4 = float(input('Digite o preço da mercadoria: R$ '))
preco_mercadoria5 = float(input('Digite o preço da mercadoria: R$ '))
preco_mercadoria6 = float(input('Digite o preço da mercadoria: R$ ')) 

total_compra = preco_mercadoria1 + preco_mercadoria2 + preco_mercadoria3 + preco_mercadoria4 + preco_mercadoria5 + preco_mercadoria6
print('Valor total da compra: R$ {:.2f}'.format(total_compra))

valor_pagar_cliente = float(input('Valor a pagar: R$ '))
print('Valor a pagar: R$ {:.2f}'.format(valor_pagar_cliente))

troco_cliente = int(total_compra - valor_pagar_cliente)

print('-'*12)
print('Escolha sua forma de pagamento: ')
print('[1] - Débito')
print('[2] - Crédito')
print('[3] - Pagamento à vista')

escolha_opcao = str(input('Escolha sua opcao: '))

print('-'*12)
print('Valor total da compra: R$ {:.2f}'.format(total_compra))
print('Valor a pagar: R$ {:.2f}'.format(valor_pagar_cliente))
print('Troco: R$ {:.2f}'.format(troco_cliente))
print('-'*12)

print('Operação realizada com sucesso!!!')



