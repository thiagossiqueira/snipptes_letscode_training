#Tuplas
# Uma tupla é uma coleção de objetos que lembra muito as listas.

# Ao invés de colchetes, usamos parênteses para declarar as tuplas:
numeros = (1,2,3,5,7,11)

# Podemos declarar sem parênteses também:
numeros = 1,2,3,5,7,11

# Para acessar um valor, utilizamos a mesma sintaxe das listas:
print(numeros[4])
print(type(numeros))

'''
Porém, tuplas são imutáveis: não é possível adicionar ou modificar valores.
Descomentar a linha abaixo provocará erro de execução:
'''
# numeros[4] = 8

# Podemos gerar uma tupla a partir de uma lista...
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
tupla1 = tuple(lista1)
print(tupla1)

# ...ou uma lista a partir de uma tupla:
tupla2 = [1, 6, 1, 8]
lista2 = list(tupla2)
print(lista2)

#Tuplas em funções
#Uma grande utilidade de tuplas é passar diversos valores para uma função. Ao utilizarmos o asterisco (*) em um argumento na definição da função, a função aceitará uma quantidade indefinida de elementos e os tratará como uma tupla.

def somatorio(*numeros):
    soma = 0
    for num in numeros:
        soma = soma + num
    return soma

s = somatorio(1,2,3,4,5,6) # estamos passando vários números
print(s) # mas deu certo mesmo assim!

#Falando no operador asterisco, ele também serve para situações opostas: Quando uma função aceita uma quantidade específica de argumentos, mas nós temos apenas uma lista ou tupla com os elementos, utilizamos o operador * para "quebrar" nossa coleção em valores individuais

def somaDeDois(a, b):
    return a + b

nums = [4, 2]

'''
Se passarmos apenas "nums" para a função somaDeDois, ela interpretará
que a variável a é a lista nums e a variável b não existe.
Teríamos que passar cada elemento de nums individualmente, o que pode ser
trabalhoso para coleções muito grandes. Porém, com o asterisco...
'''

result = somaDeDois(*nums)
print(result) # ele "quebrou" nums em 2 argumentos e a função funcionou!

#Funções com retorno múltiplo
#Vejamos um caso simples: uma função que retorna os valores máximo e mínimo de uma coleção. Você pode retornar os valores separados por vírgula. Vamos imprimir o resultado e verificar o que acontece.

def maxmin(colecao):
    maior = max(colecao)
    menor = min(colecao)
    return maior, menor

numeros = [3, 1, 4, 1, 5, 9, 2]

resposta = maxmin(numeros)
print(resposta)
print(type(resposta)) # mostra o tipo da variável resposta

#Surpresa! Ele tratou o retorno como uma tupla! Quando utilizamos valores separados por vírgula em Python, os valores são agrupados em uma tupla, mesmo que não estejamos utilizando parênteses. Essa informação é relevante porque podemos separar a tupla em varias variáveis usando a mesma sintaxe:

def maxmin(colecao):
    maior = max(colecao)
    menor = min(colecao)
    return maior, menor

numeros = [3, 1, 4, 1, 5, 9, 2]

maiorNum, menorNum = maxmin(numeros)
print(maiorNum)
print(menorNum)

#No exemplo acima é mais perceptível a sensação de que a função retornou 2 valores e o programa recebeu esses 2 valores individualmente. Por dentro, tupla. Por fora, retorno múltiplo.