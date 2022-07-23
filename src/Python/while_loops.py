#O while é bastante parecido com um 'if': ele possui uma expressão, e é executado caso ela seja verdadeira. Mas o if é executado apenas uma vez, e depois o código segue adiante.

#O while não: ao final de sua execução, ele torna a testar a expressão, e caso ela seja verdadeira, ele repete sua execução.

horario = int(input('Qual horario é agora? '))

# Testando a condição uma única vez com o if:
if 0 < horario < 6:
    print('Você está no horario da madrugada')
else:
    print('Você nao está no horario da madrugada')

# Testando a condição em loop com o while:
while 0 < horario < 6:
    print('Você está no horario da madrugada')
    horario = horario + 1
else:
    print('Você nao está no horario da madrugada')

# O while permite continuar decrementando o número de pipocas até chegar em 0:
num_pipocas = int(input('Digite o numero de pipocas: '))

while num_pipocas > 0:
    print('O numero de pipocas é: ', num_pipocas)
    num_pipocas = num_pipocas - 1