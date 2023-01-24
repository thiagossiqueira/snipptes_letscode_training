#Comentários
# Linhas iniciadas com # são comentários.
# Comentários são ignorados pelo Python e servem para explicar o código.
'''
O símbolo # é um comentário de apenas 1 linha.
Usando 3 aspas simples consecutivas é possível abrir um bloco de comentário
de múltiplas linhas. O bloco se encerra com outras 3 aspas simples.

Variáveis
Variáveis são pedacinhos de memória onde guardamos dados. Sempre que referenciamos o nome de uma variável, o dado é acessado. Criamos variáveis dando um nome a elas e usando o sinal de igual (=) para atribuir um valor.

'''

x = -10 # uma variável do tipo inteiro (int)
y = 3.14 # uma variável do tipo real (float)
escola = "Let's Code" # uma variável literal (string)
primeiraAula = True # uma variável lógica (booleana)

'''
Note que o operador igual (=) NÃO possui o mesmo comportamento da matemática. Na matemática, ele é um operador bidirecional: x = 2y seria a mesma coisa que 2y = x. No Python, ele é o que chamamos de um operador de ATRIBUIÇÃO: A expressão à direita do sinal é resolvida e seu resultado é armazenado na variável à esquerda.

Operações
'''

# Podemos fazer operações aritmeticas simples
a = 2 + 3  # Soma
b = 2 - 3  # Subtração
c = 2 * 3  # Multiplicação
d = 2 / 3  # Divisão
e = 2 // 3 # Divisão inteira
f = 2 ** 3 # Potência
g = 2 % 3  # Resto de divisão

print (a, b, c, d, e, f, g)

# Podemos fazer operações dentro do print

print (a+1, b+1)

#Podemos fazer operações com variáveis não inteiras
nome = input('Digite seu primeiro nome:')
nome = nome + ' Schmitt'
print(nome)

comparacao1 = 5 > 3
print(comparacao1)
comparacao2 = 5 < 3
print(comparacao2)

'''
Se executarmos o código acima, a saída que teremos na tela será:
True
False


Isso ocorre porque 5 é maior que 3. Portanto, comparacao1 recebeu uma expressão cujo valor lógico é verdadeiro, portanto seu resultado foi True, e o oposto ocorreu para comparacao2. O Python possui 6 operadores de comparação:

Maior que: >
Maior ou igual: >=
Menor que: <
Menor ou igual: <=
Igual: ==
Diferente: !=
Note que o operador para comparar se 2 valores são iguais é ==, e não =. Isso ocorre porque o operador = é o nosso operador de atribuição: ele diz que a variável à sua esquerda deve receber o valor da expressão à direita. O operador de == irá testar se o valor à sua esquerda é igual ao valor à sua direita e irá responder True ou False, como todos os outros operadores de comparação.

'''
