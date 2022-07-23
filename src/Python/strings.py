#Funções de strings
# Suponhamos que temos a seguinte string:

frase = 'uma FRASE'

# Podemos acessar individualmente cada caractere em uma frase.
# A ideia é a mesma de acessar uma lista:
print(frase[0])
print(frase[1])
print(frase[2])

# Os loops que usamos para listas funcionam aqui também:
for letra in frase:
    print(letra)

tamanho = len(frase)
print("A frase possui", tamanho, "caracteres")

# Porém, strings são imutáveis: não podemos alterar caracteres individuais
# A linha abaixo, se for descomentada, dará erro no programa:
# frase[4] = 'C'

# Podemos converter strings para listas:
listafrase = list(frase)
print(listafrase)

# A função join() intercala cada elemento de uma lista com uma string.
stringfinal = '-py'.join(listafrase)
print(stringfinal)

# Usar um join() com uma string vazia é útil para transformar a lista de volta
# em string:
stringfinal = ''.join(listafrase)
print(stringfinal)

# Existem algumas funções interessantes que retornam a string "tratada":
s1 = frase.capitalize() # 1a letra maiúscula, restante minúscula
s2 = frase.title() # todo início de palavra em maiúscula, resto minúscula
s3 = frase.upper() # string inteira em maiúscula
s4 = frase.lower() # string inteira em minúscula
s5 = frase.replace('F', 'C') # substitui a primeira substring pela segunda

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
# Note que NENHUMA delas ALTERA a string original, elas sempre retornam
# a string nova.
print('String original:', frase)

# Outra possibilidade com strings é quebrar a string em uma lista de substrings
# Sempre que o caractere especificado é encontrado, a string é quebrada
quebra1 = frase.split(' ') # quebra a frase no caractere espaço em branco
quebra2 = s3.split('A') # quebra a frase em maiúsculas no caractere 'A'

print(quebra1)
print(quebra2)

# Podemos inserir quebras de linha com '\n'
frase = 'uma\nFRASE'
print(frase)
# Podemos inserir tabulação com '\t'
frase = 'uma\n\tFRASE'
print(frase)
# Para conseguir representar a barra '\', precisamos de 2 barras:
frase = 'uma\\FRASE'

# Dois operadores aritméticos possuem um comportamento especial em strings:
# Operador de soma (+): concatena (une) 2 strings.
palavra1 = "Let's"
palavra2 = "Code"
palavra3 = palavra1 + palavra2
print(palavra3)

# Operador de multiplicação (*): copia uma string 'n' vezes:
palavra = 'uma'
trespalavras = 3*palavra
print(trespalavras)

#Formatação de strings
#Uma última função interessante de strings é o .format() Para entender como ela funciona, podemos pensar em um contrato. É normal que ele venha com campos em branco para serem preenchidos posteriormente. Ex:

#Eu, ____, portador do RG ____ e nascido ao dia //__, autorizo o uso de minha imagem.

#Ao inserirmos no contrato nossas informações pessoais, ele se torna completo.

#O .format() serve para "preencher" os "campos em branco" de uma string.

#Os campos em branco serão representados por pares de chave: {}

stringoriginal = 'O produto {} custa {}'
prod = 'chocolate'
preco = 3.14

# Na linha abaixo, prod substituirá o primeiro {}, e preco o segundo {}:
stringcompleta = stringoriginal.format(prod, preco)

print(stringcompleta)

# É possível colocar algumas opções especiais de formatação. Por exemplo:
stringoriginal = 'O litro da gasolina custa {:.2f}'
'''
: indica que passaremos opções
.2 indica apenas 2 casas após o ponto decimal
f indica que é um float
'''
preco = 3.14159265
stringcompleta = stringoriginal.format(preco)
print(stringcompleta)
# O preço sai com apenas 2 casas após a vírgula!

#Pode-se chamar as variávies na ordem que você quer:
str1 = '{2}, {1} and {0}'.format('a', 'b', 'c')
str2 = '{0}{1}{0}'.format('abra', 'cad')
print(str1, str2)

# Vejamos outro exemplo:
dia = 1
mes = 8
ano = 2019
data = '{}/{}/{}'.format(dia, mes, ano)
print(data)
# o dia e o mês ocupam apenas 1 espaço: 1/8/2019

# Podemos especificar um número de dígitos obrigatório por campo.
data2 = '{:2d}/{:2d}/{:4d}'.format(dia, mes, ano)
# A opção 'd' significa que o parâmetro é número inteiro.
print(data2)
# Agora dia e mês ocupam obrigatoriamente 2 espaços:  1/ 8/2019

# Podemos forçar os espaços em branco a serem preenchidos com zero:
data3 = '{:02d}/{:02d}/{:04d}'.format(dia, mes, ano)
print(data3)
# Agora sim a data está no formato usual, dd/mm/aaaa: 01/08/2019

#O .format() possui muitas opções interessantes. Há um site inteiro dedicado a explicar e exemplificar todas essas opções: https://pyformat.info/