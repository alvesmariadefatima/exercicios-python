largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede:'))
area = largura*altura
tinta = area/2

print('Para pintar esta parede, você precisará de {} L de tinta. '.format(tinta))
print('Sua parede tem a dimensão de {} x {} e sa área é de {} m².'.format(largura, altura, area))
