#Vamos entender algumas funcionalidades úteis a respeito do nosso Sistema Operacional (OS).

#Podemos utilizar o módulo "os" para acessar uma série de funções do nosso sistema operacional:

import os
#O método os.getcwd() vem de "Get current working directory" e é uma função útil para descobrirmos em qual diretório nosso arquivo .py está localizado:

print(os.getcwd())

#Podemos mudar o diretório no qual estamos usando o "Change current working directory":

os.chdir('<copiar diretorio acima>')

print(os.getcwd())

#Também podemos listar as pastas e arquivos no diretório local:

print(os.listdir())

#E criar uma nova pasta no diretório local:

os.mkdir('Pasta-OS')

# ou pastas dentro de pastas:
os.makedirs('Pasta-OS/Pasta-dentro-da-pasta')

#Também podemos remover uma ou várias camadas:

os.rmdir('Pasta-OS')
os.removedirs('Pasta-OS/Pasta-dentro-da-pasta')

#Renomear arquivos:

os.rename('teste.txt', 'novo.txt')

#Percorrer não só o nosso diretório, como os arquivos e pastas dentro dele:

for diretorio, pastas, arquivos in os.walk('<copiar diretorio local>'):
    print('Diretorio local:', diretorio)
    print('Pastas:', pastas)
    print('Arquivos:', arquivos)

#Verificar se determinada variável é um diretório ou um arquivo:

local = '<copiar diretorio local>'
print(os.path.isdir(local))
print(os.path.isfile(local))

#E, por fim, acessar o nome de determinado arquivo do nosso diretório como uma string:

print(os.path.basename(local + 'teste.txt'))