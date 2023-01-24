#Validação de entrada
#Uma utilidade interessante do while é obrigar o usuário a digitar apenas entradas válidas.

# o exemplo abaixo não aceita um salário menor do que o mínimo atual:
salario = float(input('Digite seu salario: '))
while salario < 998.0:
    salario = float(input('Entre com um salario MAIOR DO QUE 998.0: '))
else:
    print('O salario que você entrou foi: ', salario)
# o exemplo abaixo só sai do loop quando o usuário digitar "OK":
resposta = input('Digite OK: ')
while resposta != 'OK':
    resposta = input('Não foi isso que eu pedi, digite OK: ')

#Contador
#Todo tipo de código que deve se repetir várias vezes pode ser feito com o while, como somar vários valores, gerar uma sequência etc. Nestes casos, é normal utilizar um contador:

# Declaramos um contador como 0:
i = 0
# Definimos o número de repetições:
numero = int(input('Digite um numero: '))
# Rodamos o while até o contador se igualar ao número de repetições:
while i < numero:
    print(i)
    i = i+1

#Break
#Um jeito de forçar um loop a ser interrompido é utilizando o comando 'break'. O loop abaixo em tese seria infinito, mas se a condição do if for verificada, o break é executado e conseguimos escapar do loop:

while True:
    resposta = input('Digite OK: ')
    if resposta == 'OK':
        break