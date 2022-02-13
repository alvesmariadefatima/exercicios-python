frase = 'Eu adoro Python e programação'

print(frase.isupper())
print(frase.islower())

frase2 = 'I love coffee and programmer'

print(frase.isspace())
print(frase.islower())

list_of_things = list('I love coffee, computer, programmer, sleep and study')

print(list_of_things)

lista_numeros_pares = list('2', '4', '6', '8', '10', '12', '14', '16', '18', '20')
print(lista_numeros_pares)

lista_aleatoria = list('Maria de Fátima')
print(lista_aleatoria)
lista_aleatoria.sort()
print(lista_aleatoria)

lista_aleatoria = list('I love animals')
print(lista_aleatoria)
lista_aleatoria.reverse()
print(lista_aleatoria)

lista_aleatoria = list('I love animals')
print(lista_aleatoria.sort())
print(lista_aleatoria.copy())

texto = 'I love techology'
texto = texto.split('g')
print(texto)

tupla_aleatoria = [1, 3, 5, 7, 9]
print(tupla_aleatoria)

tupla_aleatoria = 1,2,3,4,5,6,7,8,9
print(tupla_aleatoria)

tupla_aleatoria = 'a', 'e', 'i', 'o', 'u'
print(tupla_aleatoria)

tupla_aleatoria = 1,3,5,7,9
print(tupla_aleatoria[4])

lista_aleatoria = [2,3,5,7,9,11,13,17]
set = set(lista_aleatoria)

set1 = {0,1,2,3,4,5,6,7,8,9}
set2 = {1,3,5,7,9,11,13,17}

print(set1 & set2) #operador and

set1 = {0,1,2,3,4,5,6,7,8,9}
set2 = {1,3,5,7,9,11,13,17}

print(set1 | set2)#operador or

l1 = [10,20,30,40,50,60,70,80]
l2 = [2,4,6,8,10,12,15,18,20]

print(l1, *l2)











