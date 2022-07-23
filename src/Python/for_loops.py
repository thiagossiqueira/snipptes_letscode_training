#Percorrendo coleções
#O for é um tipo especial de loop feito para percorrer elementos de uma coleção. Acima vimos exemplos usando um while e um contador para percorrer uma lista. O for elimina a necessidade de inicializarmos um contador, incrementarmos e verificar a condição de parada. Sintaxe:

#for (variável temporária) in (lista):
   # instruções...
   # ...

#O for se repete uma vez para cada elemento da lista. A cada repetição, a variável temporária assume o valor de um elemento da lista, na ordem da lista.

fib = [1, 1, 2, 3, 5, 8, 13]
for elemento in fib:
   print(elemento)

#Percorrendo sequências numéricas
#O for pode ser usado, junto com a função range(), para gerar sequências numéricas e contagens. Existem 3 meios de usar o range(): especificando 1, 2 ou 3 parâmetros.

# Com 1 parâmetro, ele será interpretado como valor final (exclusivo).
# O valor inicial será 0 e o incremento será 1.

for numero in range(10):
   print(numero)
   # este exemplo imprime os números de 0 a 9, de um em um

# Com 2 parâmetros, o primeiro será o valor inicial (inclusivo) e o
# segundo será o final (exclusivo).
# O incremento continuará sendo 1.

for numero in range(1,11):
   print(numero)
   # este exemplo imprime os números de 1 a 10, de um em um

# Com 3 parâmetros, o terceiro será interpretado como incremento.
for numero in range(1,20,2):
   print(numero)
   # este exemplo imprime os ímpares positivos menores do que 20
   # ele começa valendo 1 e salta de 2 em 2 até atingir ou passar 20

# O incremento pode ser também um decremento (incremento negativo).
for numero in range (10,0,-1):
   print(numero)
   #Imprimindo os números de 1 a 10 em ordem decrescente