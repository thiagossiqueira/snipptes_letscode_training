#Agrupando parâmetros
#Podemos utilizar o operador * - que, neste caso, não será uma multiplicação. Ao colocarmos o * ao lado do nome de um parâmetro na definição da função, estamos dizendo que aquele argumento será uma coleção. Mais especificamente, uma tupla. Porém, o usuário não irá passar uma tupla. Ele irá passar quantos argumentos ele quiser, e o Python automaticamente criará uma tupla com eles:

def piscina(*infos):
   vol = infos[0]*infos[1]*infos[2]
   return vol

volume = piscina(5, 4, 5)

print('O volume é: ', volume)

#Podemos utilizar o operador * na chamada da função também. Na definição, o operador * indica que devemos agrupar itens avulsos em uma coleção. Na chamada, ele indica que uma coleção deve ser expandida em itens avulsos:

def piscina(prof, largura, comprimento):
   vol = prof*largura*comprimento
   return vol

lista = [5, 4, 5]

volume = piscina(*lista)

print('O volume é: ', volume)

#Parâmetros opcionais
#Outra possibilidade são funções com parâmetros opcionais. Note que isso é diferente de termos quantidade variável de parâmetros. No caso da quantidade variável, normalmente são diversos parâmetros com a mesma utilidade (números a serem somados, valores a serem exibidos etc), enquanto os parâmetros opcionais são informações distintas que podem ou não ser passadas para a função.

#Para criar parâmetros opcionais, usaremos **, e os parâmetros passados serão agrupados em um dicionário: o nome do parâmetro será uma chave, e o valor será... O valor.

def piscina(prof, **infos):
   vol = prof*infos['largura']*infos['comprimento']
   return vol

volume = piscina(5, largura=4, comprimento=5)

print('O volume é: ', volume)

#Analogamente ao caso dos parâmetros múltiplos, é possível que o usuário da função já tenha os dados organizados em um dicionário. Neste caso, basta usar ** na chamada da função para expandir o dicionário em vários parâmetros opcionais:

def piscina(prof, largura=4, comprimento=5):
   vol = prof*largura*comprimento
   return vol

infos = {'largura': 10, 'comprimento': 20}

volume = piscina(5, **infos)

print('O volume é: ', volume)