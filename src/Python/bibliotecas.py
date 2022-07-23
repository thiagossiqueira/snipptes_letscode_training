#Bibliotecas (módulos)
#Assim como pode ser útil reaproveitar um pedaço de código em vários pontos de um mesmo programa, pode ser útil reaproveitar esse pedaço em vários outros projetos também. Várias linguagens de programação oferecem o que chamamos de bibliotecas, e em Python comumente chamamos de módulos.

#Criando módulos
#Você pode criar algumas funções dentro de um arquivo. Ao colocar esse arquivo na mesma pasta que o restante do projeto, você pode usar o comando import para informar ao programa que ele deve buscar funções naquele arquivo. A partir deste momento, você terá acesso às funções daquele módulo.

# Salve este código como contas.py
def soma(a, b):
    resultado = a + b
    return resultado

def media(x, y):
    s = soma(x, y)
    resultado = s/2
    return resultado
# Salve este outro código como principal.py na mesma pasta do contas.py
# Execute este código, não o contas.py

#import contas

#x = contas.media(3, 9)
#print(x)

#Módulos pré-instalados
#A comunidade Python costuma descrevê-lo como uma linguagem com baterias inclusas. Com isso eles querem afirmar que já vem bastante coisa pronta "de fábrica" e você não precisa fazer aquisições adicionais antes de começar a fazer muita coisa.

#Esse "bastante coisa" são bibliotecas prontas: The Python Standard Library. Tem biblioteca pra muita coisa: funções matemáticas, estatísticas, manipulação de arquivos, redes, comunicação HTTP, JSON, arquivos ZIP, arquivos CSV, codificação de texto, criptografia, HTML, interface gráfica... A lista vai embora.

#Para usar os módulos pré-instalados, basta usar import e o nome do módulo - não é necessário mover nada para nenhuma pasta. O Python saberá aonde encontrá-los! No exemplo abaixo, vamos gerar um número aleatório entre 0 e 100 utilizando a função randrange, do módulo random. Execute o código várias vezes e veja o que acontece!

import random

sorteio = random.randrange(0, 100)
print(sorteio)

#Como são vários módulos prontos, é difícil lembrar tudo que temos em mãos. Por isso, a documentação oficial recomenda manter o manual de referência dos módulos "debaixo do travesseiro": https://docs.python.org/3/library/index.html

#Instalando módulos
#O Python possui um grande repositório de módulos desenvolvidos pela comunidade. São módulos que não vem pré-instalados, mas que alguém fez e disponibilizou. Alguns desses módulos são extremamente populares e amplamente utilizados, sendo quase um consenso em suas respectivas áreas, como o matplotlib (geração de gráficos) e o pandas (manipulação de tabelas). Sempre que precisar instalar um novo módulo, basta abrir o console do seu sistema operacional (Prompt de Comando no Windows) e digitar: pip install nome-do-modulo

#Por exemplo, para instalar a matplotlib, usamos pip install matplotlib e para instalar a pandas, usamos: pip install pandas

#PS. Para abrir o seu Prompt de Comando no Windows, procure por "cmd" no menu Iniciar.

#Dica: Você pode navegar pelo repositório onde o pip encontra os módulos: https://pypi.org/