n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
média = (n1+n2)/2

if(média > 6):

    print('O aluno foi aprovado e sua média final foi {}'.format(média))

else:
    print('O aluno foi reprovado e sua média final foi {}'.format(média))