#Algumas funções podem nos ajudar a trabalhar com listas. Ao percorrermos nossa lista com um while, poderíamos usar len() caso não soubéssemos o comprimento da lista.
numeros = 10
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice = indice + 1

#Outra função útil é lista.append(), que coloca um elemento novo ao final da lista.

animais = []
resposta = 's'
while resposta == 's' or resposta == 'S':
    resposta = input('Deseja adicionar um animal à lista (s/n)? ')
    if (resposta == 's' or resposta == 'S'):
        animal = input('Digite o nome do animal: ')
        animais.append(animal) # adiciona o novo animal à lista
print(animais)

#A função lista.remove() deleta um elemento da lista. (mas dá erro se o elemento não existir).

animal = input('Digite o animal a ser deletado da lista: ')
animais.remove(animal)
print(animais)

#Algumas outras funções úteis:

#lista.count() conta quantas vezes um elemento aparece.
jogadores = ['Ronaldo', 'Rivaldo', 'Ronaldo', 'Adriano']
ronaldos = jogadores.count('Ronaldo')
print(jogadores)
print('Quantidade de Ronaldos: ', ronaldos)

#lista.index() busca em um elemento e fala em qual posição ele aparece.
rivaldo = jogadores.index('Rivaldo')
print("Rivaldo está na posição ", rivaldo)

#lista.sort() ordena uma lista.
jogadores.sort()
print("jogadores em ordem alfabética: ", jogadores)

#As funções max(lista) e min(lista) obtém, respectivamente, o maior e o menor valor.
digitos = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maior = max(digitos)
menor = min(digitos)
print(digitos)
print("Maior = ", maior, "e menor = ", menor)