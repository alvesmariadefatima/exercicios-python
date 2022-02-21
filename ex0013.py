salário_funcionario = float(input('Digite o salário do funcionário? R$ '))
porcentagem = salário_funcionario + (salário_funcionario*15/100)

print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'.format(salário_funcionario, porcentagem))
