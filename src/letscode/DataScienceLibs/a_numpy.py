#Numpy é uma biblioteca das principais bibliotecas do Python. Devido à sua grande praticidade e eficiência, ela é extremamente utilizada para computação científica e análise de dados. Esta fama se dá principalmente à estrutura chamada numpy array, uma forma eficiente de guardar e manipular matrizes, que serve como base para as tabelas que iremos utilizar.

#1. Arrays
import numpy as np

# criando arrays do numpy a partir de listas do python
lista = [1,2,3,4,5]
listaNumpy = np.array(lista)
print(listaNumpy)

#Criando array zeros numpy
zeros = np.zeros(10)

#Criando array com 1s
uns = np.ones(10)

#Criando array de um numero qualquer
cincos = np.ones(10) * 5

#Criando array com sequencia
lista10 = np.arange(0,10)

#Criando array com saltos
listaD = np.arange(0,20,2)

#Array espaçado, os dois primeiros numeros são o intervalo, o terceiro é o número de valores
np.linspace(0,1,20)

#Criando array com valores aleatorios
aleatorio = np.random.rand(20)

# aleatorio inteiro (10 itens de 0 a 100)
lista1 = np.random.randint(0,100,10)

#Indexação
x = lista10[5]

#Partindo array
y = lista10[2:7]

#Criando array com sequencia
lista40 = np.arange(10,50)


# Operações simples
lista1 * 2
lista1 + 1
lista1 ** 2
lista1 / 2
#soma
lista2 = np.random.randint(0,100,10)
lista1 + lista2
# divisão
lista1 / lista2
# mult
lista1 * lista2

#Funções sobre um array
#maior valor
lista1.max()
#local do maior valor
lista1.argmax()
#maior valor
lista1.min()
#local do menor valor
lista1.argmin()
#soma de todos os itens
lista1.sum()
#media
lista1.mean()
#desvio padrão
lista1.std()
#ordenar a lista
lista1.sort()

#Trocando o tipo dos dados na lista
lista1 = lista1.astype(int)

#2. Matrizes
listaD = np.arange(0,20,2)
#Criando matriz
matriz = listaD.reshape(5, 2)

#mostra qual é o formato da matriz
z = matriz.shape

#Criando matriz identidade
mIdentidade = np.eye(5)

#indexação matriz
t = matriz[2:,1:]
#Mascaras
criterio = matriz > 5

i = matriz[criterio]
#Numeros pares
pares = lista10 % 2 == 0

#Aplicando a máscara à matriz
r = lista10[pares]
#Aplicando a máscara maior que 2
lista10[lista10>2]